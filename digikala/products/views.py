from rest_framework.exceptions import bad_request
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from django.http import JsonResponse

from api_digikala import get_url_cleaned_data, get_product_id, get_url_maker
from api_digikala.url_maker import URL_TYPES

from .models import Laptop, Mobile
from .serializer import LaptopSerializer, MobileSerializer
from .utils import extract_laptop, extract_mobile


class ProductListAPIView(generics.GenericAPIView):
    serializer_classes = {
        "notebook-netbook-ultrabook": LaptopSerializer,
        "mobile-phone": MobileSerializer,
    }

    models = {
        "notebook-netbook-ultrabook": Laptop,
        "mobile-phone": Mobile,
    }

    extractors = {
        "notebook-netbook-ultrabook": extract_laptop,
        "mobile-phone": extract_mobile,
    }

    def _setup(self, category):
        self.model = self.models[category]
        self.serializer_class = self.serializer_classes[category]
        self.extractor = self.extractors[category]

    @property
    def url(self):
        url = self.request.data.get("url")
        if not url:
            return bad_request(self.request, Exception)
        return url

    def get_queryset(self):
        pass

    def get_object(self):
        url_type, _ = get_url_maker(self.url)
        if url_type == URL_TYPES.PRODUCT:
            p_id = get_product_id(self.url)

            qs = Laptop.objects.filter(product_id__exact=int(p_id))
            if qs.exists():
                return qs.first()

            qs = Mobile.objects.filter(product_id__exact=int(p_id))
            if qs.exists():
                return qs.first()

    def post(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as e:
            return JsonResponse({"error": "Invalid or not supported url"}, status=status.HTTP_400_BAD_REQUEST)
        if obj:
            serializer = self.serializer_classes[obj.category]
            return JsonResponse(serializer(obj).data, status=status.HTTP_200_OK)

        try:
            data = get_url_cleaned_data(self.url)
        except Exception as e:
            return JsonResponse({"error": "Invalid or not supported url"}, status=status.HTTP_400_BAD_REQUEST)

        self._setup(data.get("category"))

        products = data.get("products")
        if products:
            res = []
            for p in data.get("products"):
                try:
                    cleaned_data = self.extractor(p)
                except Exception:
                    continue
                res.append(cleaned_data)
                obj = self.model.objects.get_or_create(**cleaned_data)
            return JsonResponse(res, safe=False, status=status.HTTP_200_OK)

        else:
            cleaned_data = self.extractor(data)
            self.model.objects.get_or_create(**cleaned_data)
            return JsonResponse(cleaned_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "only POST allowed"})

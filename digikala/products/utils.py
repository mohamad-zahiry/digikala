def rnlt(text: str):
    """remove new line and tab"""
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    text = text.rstrip()
    text = text.lstrip()
    return text


def extract_laptop(data: dict):
    details = data.get("details")
    return {
        "product_id": data.get("product_id", ""),
        "category": rnlt(data.get("category", "")),
        "title": rnlt(data.get("title", "")),
        "brand": rnlt(data.get("brand", "")),
        "price": data.get("price", ""),
        "off": data.get("off", ""),
        "url": rnlt(data.get("url", "")),
        "cpu_manifacturer": rnlt(" ".join(details.get("سازنده پردازنده", ""))),
        "cpu_serry": rnlt(" ".join(details.get("سری پردازنده", ""))),
        "cpu_model": rnlt(" ".join(details.get("مدل پردازنده", ""))),
        "ram_capacity": rnlt(" ".join(details.get("ظرفیت حافظه RAM", ""))),
        "ram_type": rnlt(" ".join(details.get("نوع حافظه RAM", ""))),
        "gpu_manifacturer": rnlt(" ".join(details.get("سازنده پردازنده گرافیکی", ""))),
        "gpu_model": rnlt(" ".join(details.get("مدل پردازنده گرافیکی", ""))),
        "internal_sotrage_type": rnlt(" ".join(details.get("نوع حافظه داخلی", ""))),
        "size": rnlt(" ".join(details.get("ابعاد", ""))),
        "resolution": rnlt(" ".join(details.get("اندازه صفحه نمایش", ""))),
        "optical_drive": rnlt(" ".join(details.get("درایو نوری", ""))),
        "connection_ports": rnlt(" ".join(details.get("درگاه‌های ارتباطی", ""))),
        "usb2": rnlt(" ".join(details.get("تعداد پورت USB 2.0", ""))),
        "usb3": rnlt(" ".join(details.get("تعداد پورت USB 3.0", ""))),
        "battery": rnlt(" ".join(details.get("توضیحات باتری", ""))),
    }


def extract_mobile(data: dict):
    details = data.get("details")
    return {
        "product_id": data.get("product_id"),
        "category": rnlt(data.get("category")),
        "title": rnlt(data.get("title")),
        "brand": rnlt(data.get("brand")),
        "price": data.get("price"),
        "off": data.get("off"),
        "url": rnlt(data.get("url")),
        "cpu": rnlt(" ".join(details.get("پردازنده‌ی مرکزی"))),
        "ram": rnlt(" ".join(details.get("مقدار RAM"))),
        "size": rnlt(" ".join(details.get("ابعاد"))),
        "resolution": rnlt(" ".join(details.get("رزولوشن"))),
        "storage": rnlt(" ".join(details.get("حافظه داخلی"))),
        "network": rnlt(" ".join(details.get("شبکه های ارتباطی"))),
        "main_camera": rnlt(" ".join(details.get("رزولوشن عکس"))),
        "selfie_camera": rnlt(" ".join(details.get("دوربین سلفی"))),
        "battery": rnlt(" ".join(details.get("مشخصات باتری"))),
    }

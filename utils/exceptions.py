from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 403:
            response.data = {
                "detail": "Sizda bu amalni bajarish uchun ruxsat yo'q.",
                "status_code": 403
            }
        elif response.status_code == 400:
            response.data = {
                "error": "Noto‘g‘ri ma’lumot yuborildi.",
                "details": response.data
            }

    return response

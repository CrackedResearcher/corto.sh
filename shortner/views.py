from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UrlReadSerializer, UrlCreateSerializer
from .services import url_services


class UrlShortnerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UrlReadSerializer
        
        user = request.user
        data = url_services.get_url_data(user=user)
        res = (serializer(data, many=True)).data
        print("ressss ===> ", res)
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        serializer = UrlCreateSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                print("===== data =>>>", serializer.data)

                data, exists = url_services.create_url(serializer.data, user)
                if data:
                    print("====== try success data ====", data)
                    write_serializer = UrlCreateSerializer(data)
                    return Response(write_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": exists}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UrlUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = request.user
        data = url_services.get_url_details(id, user)
        serializer = UrlReadSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = request.user
        serializer = UrlCreateSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                print("URL UPDATED ===> ", serializer.data)
                updated_data = url_services.update_url_details(serializer.validated_data, id, user)
                if updated_data is None:
                    return Response({"error": "Url doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
                read_serializer = UrlReadSerializer(updated_data)
                return Response(read_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = request.user
        success, message = url_services.delete_url_data(id, user)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"error": message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UrlAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

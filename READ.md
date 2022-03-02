How to use mozio api

Providers:

1.List all providers:https://mozio.pythonanywhere.com/providers/?format=json
2.Create provider: https://mozio.pythonanywhere.com/provider-create/ (method POST, password must be hashed, all providers will recive an unique token automatically)
{
        "surname": "",
        "last_name": "",
        "phone_number": "",
        "email": "",
        "language": "",
        "currency": "",
        "password": ""
}
3.Update provider:  https://mozio.pythonanywhere.com/provider-update/<str:tk>/ ( method PUT, <str:tk> must be provided provider unique token)
{
        "tk": "",
        "surname": "",
        "last_name": "",
        "phone_number": "",
        "email": "",
        "language": "",
        "currency": "",
        "password": ""
}

4.Update provider:  https://mozio.pythonanywhere.com/provider-retrive/<str:tk>/ ( method GET, <str:tk> must be provided provider unique token)

5.Delete provider:  https://mozio.pythonanywhere.com/provider-delete/<str:tk>/'( method DELETE)



Service Area:

1.List all service areas: https://mozio.pythonanywhere.com/services/?format=json

2.Create service area: https://mozio.pythonanywhere.com/services/service-create/ 
method POST, provider = provider token, 
coordinates example = [[30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]] - attention! first list and last must be the same(polygon ruls)
 {
        "provider": "",
        "polygon_name": "",
        "price": "",
        "coordinates": ""
    }
3.Update service area: https://mozio.pythonanywhere.com/servicesservice-update/<str:tk>/ (method PUT, provider = provider token)
{
        "provider": "",
        "polygon_name": "",
        "price": "",
        "coordinates": ""
    }

4.Delete service area: https://mozio.pythonanywhere.com/services/service-delete/<str:tk>/ (method DELETE, provider = provider token)


5. Check if a point (lat\lon) are inside of any area and return areas that contains point: this part you can test only, not included in Git


For testing you can use: 
1. Use http://geojson.io/ to create an polygon, and take all coordinates in this geojson format: 

2. [[-115.224609375,34.88593094075317],[-100.546875,34.88593094075317],[-100.546875,46.37725420510028],[-115.224609375,46.37725420510028],[-115.224609375,34.88593094075317]]

3. create a new service area:  https://mozio.pythonanywhere.com/services/service-create/ (use POST method and insert json in the request body with new coordinates, like this:

4. {
        "provider": "36b8c7c2-37bb-4519-82ab-8a9e17a40701",
        "polygon_name": "pole78786r4",
        "price": "10800",
        "coordinates": "[[-115.224609375,34.88593094075317],[-100.546875,34.88593094075317],[-100.546875,46.37725420510028],[-115.224609375,46.37725420510028],[-115.224609375,34.88593094075317]]"
    }
5. Use http://geojson.io/ to create a point in the middle of polygon, and take coordinates of the point in this format: -104.32617187499999,40.245991504199026

6. Use new coordinated like in this example: https://mozio.pythonanywhere.com/services/service/-104.32617187499999,40.245991504199026?format=json    (method GET)

7. It will return a json with your service area that you create or more if the point are in multiple service areas









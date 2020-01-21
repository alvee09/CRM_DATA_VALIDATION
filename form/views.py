from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import shipment_details, supplier_details
def index(request):
    supplier_list = supplier_details.objects.all()
    context= {'supplier_list': supplier_list}
    return render(request, 'form/index.html', context)

def add_details(request):
    reinitialize = shipment_details.objects.filter(isReviewed = 0)
    for i in reinitialize:
        i.isReviewed = 1
        i.save()
    PONumber= request.POST['PONumber']
    SupName = request.POST['SupName']
    SupAddress = request.POST['SupAddress']
    USIMno = request.POST['USIMno']
    Composition = request.POST['Composition']
    ClothingStructure = request.POST['ClothingStructure']
    MerchandiseDescription = request.POST['MerchandiseDescription']
    PaymentCondition = request.POST['PaymentCondition']
    TransportationMethod = request.POST['TransportationMethod']
    DeliveryCondition = request.POST['DeliveryCondition']
    GrossWeight = request.POST['GrossWeight']
    NetWeight = request.POST['NetWeight']
    #GwNwRatio = request.POST['GwNwRatio']
    carton = request.POST['carton']
    quantity = request.POST['quantity']
    UnitPrice = request.POST['UnitPrice']
    currency = request.POST['currency']
    TotalAmount = request.POST['TotalAmount']
    PackOrSet = request.POST['PackOrSet']
    UnitPriceBreakdown = request.POST['UnitPriceBreakdown']
    pig = request.POST['pig']
    CoO = request.POST['CoO']
    PackingMethod = request.POST['PackingMethod']
    HSCode = request.POST['HSCode']

    GwNwRatio = int(GrossWeight) / int(NetWeight)
    create = shipment_details(
        PONumber= PONumber,
        SupNam = SupName,
        SupAddress = SupAddress,
        USIMno = USIMno,
        Composition = Composition,
        ClothingStructure = ClothingStructure,
        MerchandiseDescription = MerchandiseDescription,
        PaymentCondition = PaymentCondition,
        TransportationMethod = TransportationMethod,
        DeliveryCondition = DeliveryCondition,
        GrossWeight = GrossWeight,
        NetWeight = NetWeight,
        GwNwRatio = GwNwRatio,
        carton = carton,
        quantity = quantity,
        UnitPrice = UnitPrice,
        currency = currency,
        TotalAmount = TotalAmount,
        PackOrSet = PackOrSet,
        UnitPriceBreakdown = UnitPriceBreakdown,
        pig = pig,
        CoO = CoO,
        PackingMethod = PackingMethod,
        HSCode = HSCode
    )
    create.save()

    #return render(request, 'form/success.html')
    #index(request)
    #return HttpResponseRedirect(reverse('form:index'))
    queryset = shipment_details.objects.filter(isReviewed = 0)
    supplier_list = supplier_details.objects.filter(RexNo = queryset[0].SupNam)
    context= {'shipment': queryset, 'supplier':supplier_list}
    print(context)
    return render(request, 'form/review.html', context)

def api_response(request, pk):
    queryset = shipment_details.objects.filter(id = pk).values()
    json = queryset[0]
    print(json)
    return JsonResponse(json, safe = False)

def getSuggestions(request):
    name = request.GET.get('name')
    name = name.upper()
    print(name)
    input_data = supplier_details.objects.filter(SupplierName__contains = name).values()
    print(input_data)
    data = list(input_data)
    #serializers.serialize("json", input_data, fields = ('id', 'SupplierName')) 
    #serializers.serialize('json', input_data)
    return JsonResponse(data, safe = False)

def getAddress(request):
    rex = request.GET.get('rex')
    address = supplier_details.objects.filter(RexNo = rex).values()
    print(address)
    address = list(address)
    return JsonResponse(address, safe= False)

def reviewed(request):
    queryset = shipment_details.objects.get(isReviewed = 0)
    print(queryset)
    queryset.isReviewed = 1
    queryset.save()
    return HttpResponseRedirect(reverse('form:index'))

def edit(request):
    queryset = shipment_details.objects.filter(isReviewed = 0)
    supplier_list = supplier_details.objects.filter(RexNo = queryset[0].SupNam)
    context= {'shipment': queryset, 'supplier':supplier_list}
    print(context)
    return render(request, 'form/edit.html', context)

def finalInput(request):
    PONumber = request.POST['PONumber']
    SupName = request.POST['SupName']
    SupAddress = request.POST['SupAddress']
    USIMno = request.POST['USIMno']
    Composition = request.POST['Composition']
    ClothingStructure = request.POST['ClothingStructure']
    MerchandiseDescription = request.POST['MerchandiseDescription']
    PaymentCondition = request.POST['PaymentCondition']
    TransportationMethod = request.POST['TransportationMethod']
    DeliveryCondition = request.POST['DeliveryCondition']
    GrossWeight = request.POST['GrossWeight']
    NetWeight = request.POST['NetWeight']
    #GwNwRatio = request.POST['GwNwRatio']
    carton = request.POST['carton']
    quantity = request.POST['quantity']
    UnitPrice = request.POST['UnitPrice']
    currency = request.POST['currency']
    TotalAmount = request.POST['TotalAmount']
    PackOrSet = request.POST['PackOrSet']
    UnitPriceBreakdown = request.POST['UnitPriceBreakdown']
    pig = request.POST['pig']
    CoO = request.POST['CoO']
    PackingMethod = request.POST['PackingMethod']
    HSCode = request.POST['HSCode']

    shipment = shipment_details.objects.filter(PONumber = PONumber)
    print("inside final input")
    GwNwRatio = float(GrossWeight) / float(NetWeight)
    shipment.update(
        PONumber= PONumber,
        SupNam = SupName,
        SupAddress = SupAddress,
        USIMno = USIMno,
        Composition = Composition,
        ClothingStructure = ClothingStructure,
        MerchandiseDescription = MerchandiseDescription,
        PaymentCondition = PaymentCondition,
        TransportationMethod = TransportationMethod,
        DeliveryCondition = DeliveryCondition,
        GrossWeight = GrossWeight,
        NetWeight = NetWeight,
        GwNwRatio = GwNwRatio,
        carton = carton,
        quantity = quantity,
        UnitPrice = UnitPrice,
        currency = currency,
        TotalAmount = TotalAmount,
        PackOrSet = PackOrSet,
        UnitPriceBreakdown = UnitPriceBreakdown,
        pig = pig,
        CoO = CoO,
        PackingMethod = PackingMethod,
        HSCode = HSCode,
        isReviewed = 1
    )
    return HttpResponseRedirect(reverse('form:index'))
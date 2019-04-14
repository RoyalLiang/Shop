from django.http import HttpResponse
from import_export import resources
from viewsCount.models import *


class VisitorResource(resources.ModelResource):
    class Meta:
        model = Visitor

    def export_csv(request):
        view_resource = VisitorResource()
        dataset = view_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="views_visitor.csv"'
        return response

    def export_excel(request):
        excel_resource = VisitorResource()
        dataset = excel_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="visitor.xls"'
        return response

    def export_json(request):
        json_resource = VisitorResource()
        dataset = json_resource.export()
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="visitor.json"'
        return response

    def export_yaml(request):
        yaml_resource = VisitorResource()
        dataset = yaml_resource.export()
        response = HttpResponse(dataset.yaml, content_type='application/yaml')
        response['Content-Disposition'] = 'attachment; filename="visitor.yaml"'
        return response


class RegionByDayResource(resources.ModelResource):
    class Meta:
        model = RegionByDay

    def export_csv(request):
        view_resource = RegionByDayResource()
        dataset = view_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="region.csv"'
        return response

    def export_excel(request):
        excel_resource = RegionByDayResource()
        dataset = excel_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="region.xls"'
        return response

    def export_json(request):
        json_resource = RegionByDayResource()
        dataset = json_resource.export()
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="region.json"'
        return response

    def export_yaml(request):
        yaml_resource = RegionByDayResource()
        dataset = yaml_resource.export()
        response = HttpResponse(dataset.yaml, content_type='application/yaml')
        response['Content-Disposition'] = 'attachment; filename="region.yaml"'
        return response


class DeviceByDayResource(resources.ModelResource):
    class Meta:
        model = DeviceByDay

    def export_csv(request):
        device_resource = DeviceByDayResource()
        dataset = device_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="device.csv"'
        return response

    def export_excel(request):
        excel_resource = DeviceByDayResource()
        dataset = excel_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="device.xls"'
        return response


class ReferByDayResource(resources.ModelResource):
    class Meta:
        model = ReferByDay

    def export_csv(request):
        csv_resource = ReferByDayResource()
        dataset = csv_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="refer.csv"'
        return response

    def export_excel(request):
        excel_resource = ReferByDayResource()
        dataset = excel_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="refer.xls"'
        return response
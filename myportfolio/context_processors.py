def global_settings(request):
    from .models import HomeSidebarInfo
    
    # Get data you want available in all templates
    sideBarItem = HomeSidebarInfo.objects.first
    
    return {
        'sideBarItem': sideBarItem
    }
from .models import Illustration, Tools

def seeder_func():

    tools = [
        'Procreate',
        'Adobe Illustrator',
        'Adobe Photoshop', 
        'Adoebe After Effects'
    ]
 
    for tool in tools :

       if Tools.objects.filter(name=tool):
           pass
       else:
           new_tool = Tools(name=tool)
           new_tool.save()
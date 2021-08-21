
import django
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s28.settings")
django.setup()

from web import models
models.Eachclass.objects.create(Thatclass='第一节',Earnestpeopl=16,Focusvalue=18)
models.Eachclass.objects.create(Thatclass='第二节',Earnestpeopl=17,Focusvalue=17)
models.Eachclass.objects.create(Thatclass='第三节',Earnestpeopl=16,Focusvalue=18)
models.Eachclass.objects.create(Thatclass='第四节',Earnestpeopl=17,Focusvalue=18)
models.Eachclass.objects.create(Thatclass='第五节',Earnestpeopl=16,Focusvalue=19)
models.Eachclass.objects.create(Thatclass='第六节',Earnestpeopl=17,Focusvalue=18)
models.Eachclass.objects.create(Thatclass='第七节',Earnestpeopl=16,Focusvalue=18)
models.Eachclass.objects.create(Thatclass='第八节',Earnestpeopl=17,Focusvalue=20)


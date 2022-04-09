from django.db import models


CAR_NUMBERS = (
    ("90018WAA", "90 018WAA"),
    ("90Y054NA", "90 Y054NA"),
    ("90E077HA", "90 E077HA"),
    ("90H084PA", "90 H084PA"),
    ("90087FBA", "90 087FBA"),
    ("90S087KA", "90 S087KA"),

    ("90G350LA", "90 G350LA"),
    ("90100BAA", "90 100BAA"),
    ("90102WAA", "90 102WAA"),
    ("90200BAA", "90 200BAA"),
    ("90206WAA", "90 206WAA"),
    ("90255WAA", "90 255WAA"),

    ("90279FBA", "90 279FBA"),
    ("90280FBA", "90 280FBA"),
    ("90281FBA", "90 281FBA"),
    ("90283FBA", "90 283FBA"),
    ("90C285OA", "90 C285OA"),
    ("90C285OA", "90 C285OA"),

    ("90M287OA", "90 M287OA"),
    ("90A297LA", "90 A297LA"),
    ("90315WAA", "90 315WAA"),
    ("90316WAA", "90 316WAA"),
    ("01Q370PA", "01 Q370PA"),

    ("90468WAA", "90 468WAA"),
    ("90469WAA", "90 469WAA"),
    ("90M469MA", "90 M469MA"),
    ("90481WAA", "90 481WAA"),
    ("90482WAA", "90 482WAA"),

    ("90M484LA", "90 M484LA"),
    ("90R490BA", "90 R490BA"),
    ("90P064PA", "90 P064PA"),
    ("90615WAA", "90 615WAA"),
    ("90A641LA", "90 A641LA"),
    ("90J651OA", "90 J651OA"),

    ("90Z669EA", "90 Z669EA"),
    ("90J689OA", "90 J689OA"),
    ("90K716NA", "90 K716NA"),
    ("90G768EA", "90 G768EA"),
    ("90J770JA", "90 J770JA"),
    ("90795WAA", "90 795WAA"),

    ("90D832LA", "90 D832LA"),
    ("90A832PA", "90 A832PA"),
    ("90833ABA", "90 833ABA"),
    ("90D893NA", "90 D893NA"),
    ("90C962KA", "90 C962KA"),
    ("90R990LA", "90 R990LA"),
)


class Data(models.Model):


    fio = models.TextField(verbose_name="Haydovchi F.I.O?",)
    carnumber = models.CharField(max_length = 60,choices = CAR_NUMBERS,default = "",verbose_name="Mashina raqami?",)
    regdata = models.DateField(verbose_name="Berilgan sanasi?",)
    tirnumber = models.TextField(blank=True, verbose_name="TIR raqami? (agar bo'lsa)",)
    waybill = models.TextField(blank=True, verbose_name="Yo'l varaqasi raqami? (agar bo'lsa)",)
    cmr1 = models.TextField(blank=True, verbose_name="CMR raqami? (agar bo'lsa)",)
    cmr2 = models.TextField(blank=True, verbose_name="CMR raqami(agar CMR bittadan ko'p bo'lsa)?",)
    dazvol = models.TextField(blank=True, verbose_name="Dozvol raqami?",)
    tc = models.TextField(blank=True, verbose_name="КОМАНДИРОВОЧНОЕ УДОСТОВЕРЕНИЕ? (agar bo'lsa)",)
    tircheck = models.BooleanField(verbose_name="TIR Check",)
    waybillcheck = models.BooleanField(verbose_name="WayBill Check",)
    cmr1check = models.BooleanField(verbose_name="CMR Check",)
    cmr2check = models.BooleanField(verbose_name="CMR-2 Check",)
    dcheck = models.BooleanField(verbose_name="Dozvol Check",)
    tcheck = models.BooleanField(verbose_name="К/У")
    checker = models.BooleanField(verbose_name="Check All",)

    class Meta:
        verbose_name = 'Hujjat '
        verbose_name_plural = "Hujjatlar"

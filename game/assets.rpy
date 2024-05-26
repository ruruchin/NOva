#Описание персонажей
define effi = Character('Эффи', color="#000000")
define gg = Character('[gg]', color="#000000")

#Описание спрайтов для подсвечивания говорящего
init python:
    kidzuki = CHBM(_("kidzuki_smile1"), tag="kidzuki_smile1", color="#000000")
    kidzuki = CHBM(_("kidzuki_smile2"), tag="kidzuki_smile2", color="#000000")
    kidzuki = CHBM(_("kidzuki_smile3"), tag="kidzuki_smile3", color="#000000")
    kidzuki = CHBM(_("kidzuki_netral1"), tag="kidzuki_netral1", color="#000000")
    kidzuki = CHBM(_("kidzuki_netral2"), tag="kidzuki_netral2", color="#000000")
    kidzuki = CHBM(_("kidzuki_netral3"), tag="kidzuki_netral3", color="#000000")

    noe = CHBM(_("noe_konfused"), tag="noe_konfused", color="#000000")
    noe = CHBM(_("noe_konfused2"), tag="noe_konfused2", color="#000000")
    noe = CHBM(_("noe_smile1"), tag="noe_smile1", color="#000000")
    noe = CHBM(_("noe_smile2"), tag="noe_smile2", color="#000000")
    noe = CHBM(_("noe_netral"), tag="noe_netral", color="#000000")   

#Описание эмоций
'''Счастье'''
image effi_smile_bok ="images/Effi_emo/bok/4.png"
image effi_smile_pod = "images/Effi_emo/pod/1.png"
image effi_smile_riad = "images/Effi_emo/riad/1.png"
image effi_smile_u =  "images/Effi_emo/u/1.png"
image effi_smile_za = "images/Effi_emo/za/1.png"
image effi_smile_pod2 = "images/Effi_emo/pod/5.png"

'''Недовольство'''
image effi_no_bok ="images/Effi_emo/bok/1.png"
image effi_no_pod = "images/Effi_emo/pod/4.png"
image effi_no_riad = "images/Effi_emo/riad/4.png"
image effi_no_u =  "images/Effi_emo/u/4.png"
image effi_no_za = "images/Effi_emo/za/4.png"
image effi_no_riad2 = "images/Effi_emo/riad/2.png"

image noe_konfused = "images/Noe/konfused.png"
image noe_konfused2 = "images/Noe/konfused2.png"

'''Довольство'''
image effi_happy_bok ="images/Effi_emo/bok/5.png"
image effi_happy_pod = "images/Effi_emo/pod/1.png"
image effi_happy_riad = "images/Effi_emo/riad/5.png"
image effi_happy_u =  "images/Effi_emo/u/5.png"
image effi_happy_za = "images/Effi_emo/za/3.png"

image kidzuki_smile1 = "images/Kidzuki/smile1.png"
image kidzuki_smile2 = "images/Kidzuki/smile2.png"
image kidzuki_smile3 = "images/Kidzuki/smile3.png"

image noe_smile1 = "images/Noe/smile1.png"
image noe_smile2 = "images/Noe/smile2.png"

"""Нейтральные"""
image effi_netral_bok ="images/Effi_emo/bok/2.png"
image effi_netral_pod = "images/Effi_emo/pod/4.png"
image effi_netral_riad = "images/Effi_emo/riad/4.png"
image effi_netral_u =  "images/Effi_emo/u/2.png"
image effi_netral_za = "images/Effi_emo/za/5.png"
image effi_netral_pod2 = "images/Effi_emo/pod/2.png"

image kidzuki_netral1 = "images/Kidzuki/netral1.png"
image kidzuki_netral2 = "images/Kidzuki/netral2.png"
image kidzuki_netral3 = "images/Kidzuki/netral3.png"

image noe_netral = "images/Noe/netral.png"

"""Зубы"""
image effi_teeth_bok ="images/Effi_emo/bok/3.png"
image effi_teeth_pod = "images/Effi_emo/pod/3.png"
image effi_teeth_riad = "images/Effi_emo/riad/3.png"
image effi_teeth_u =  "images/Effi_emo/u/3.png"
image effi_teeth_za = "images/Effi_emo/za/2.png"

#Описание сцен с убйиством
image bg kitchen_top = "bg kitchen_top.png"
image bg kitchen_bottom = "bg kitchen_bottom.png"

image effi_kitchen_coock = "effi_kitchen_coock.png"
image effi_kitchen_behind = "effi_kitchen_behind.png"
image effi_kitchen_behind_knife = "effi_kitchen_behind_knife.png"

image mother_kitchen_cook = Glitch("mother_kitchen_cook.png", _fps=5)
image mother_kitchen_behind = Glitch("mother_kitchen_behind.png", _fps=5)
image mother_kitchen_behind_knife = Glitch("mother_kitchen_behind_knife.png", _fps=5)
image glitch_mother_kitchen_floor = Glitch("mother_kitchen_floor.png", _fps=5)
image mother_kitchen_floor = "mother_kitchen_floor.png"

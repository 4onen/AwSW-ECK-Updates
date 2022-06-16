import renpy
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod
from modloader.modinfo import get_mods

@loadable_mod
class AWSWMod(Mod):
    name = "Savior"
    version = "v1.2.5"
    author = "EvilChaosKnight"
    nsfw = False

    def mod_load(self):
        brsource = ml.search_peak_if(modast.find_say("Bryce led me to the dig site where they had unearthed the building's entry. Once we got nearer, he stayed behind and motioned for me to go forward."), ast.Scene, 100)
        bryce_hook = modast.find_label("eck_common_bryce")
        hook = modast.hook_opcode(brsource, None)
        modast.call_hook(brsource, bryce_hook, None)
        hook.chain(modast.find_label("mainmenu"))
        
        brsource2 = ml.search_peak_if(modast.find_say("But I won't ever stop looking for those who are responsible for this, and if I find them, I will show no mercy."), ast.Label, 100)
        bryce_hook2 = modast.find_label("eck_common_brycemv")
        hook = modast.hook_opcode(brsource2, None)
        modast.call_hook(brsource2, bryce_hook2, None)

    def mod_complete(self):
        if "Chaos_Knight core mod." not in get_mods():
            raise Exception("Chaos_Knight's core mod not found. This mod is required by %s" % " ".join(self.mod_info()))
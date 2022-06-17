import renpy
import renpy.ast as ast
import renpy.sl2.slast as slast
import renpy.parser as parser
import sys
from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod
from modloader.modinfo import get_mods

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Not-so-Tragic Hero", "v2.1.6", "EvilChaosKnight")

    def mod_load(self):
        source = ml.search_peak_if(modast.find_say("In the weeks that followed, the dragons prepared for the comet."), ast.Scene, 100)
        anna_hook = modast.find_label("eck_common_anna")
        hook = modast.hook_opcode(source, None)
        modast.call_hook(source, anna_hook, None)
        hook.chain(modast.search_for_node_type(source, ast.Scene))
        
        tocompile = """
        screen dummy:
            if persistent.eckannacured:
                add "image/ui/title/eckannacuredending.png"
        """
        compiled = parser.parse("FNDummy", tocompile)
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    modast.get_slscreen('main_menu').children.append(child)

    def mod_complete(self):
        if "Chaos_Knight core mod." not in get_mods():
            raise Exception("Chaos_Knight's core mod not found. This mod is required by %s" % " ".join(self.mod_info()))
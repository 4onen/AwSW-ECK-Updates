from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml


@loadable_mod
class AWSWMod(Mod):
    name = "Savior"
    version = "v1.2.5"
    author = "EvilChaosKnight"
    dependencies = ["MagmaLink", "Chaos_Knight core mod."]

    @staticmethod
    def mod_load():
        ( ml.find_label('bryce5')
            .search_say("Bryce led me to the dig site where they had unearthed the building's entry. Once we got nearer, he stayed behind and motioned for me to go forward.")
            .search_scene(depth=100)
            .hook_to('eck_common_bryce')
        )

        ( ml.find_label('passontestresults')
            .hook_to('eck_common_brycemv')
        )

    @staticmethod
    def mod_complete():
        pass

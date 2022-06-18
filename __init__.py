from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml


@loadable_mod
class AWSWMod(Mod):
    name = "Not-so-Tragic Hero"
    version = "v2.1.6"
    author = "EvilChaosKnight"
    dependencies = ["MagmaLink", "Chaos_Knight core mod."]

    def mod_load(self):
        (ml.find_label('annagoodending')
            .search_say("In the weeks that followed, the dragons prepared for the comet.")
            .search_scene(depth=100)
            .hook_to('eck_common_anna')
            .search_say("No doubt, it would be a risk to relive this rollercoaster of emotions. After all, I would have to go through all the events and their dangers again, but maybe it would be worth it...")
            .link_behind_from('eck_anna_stockcredits2')
            .search_scene('black')
            .link_from('eck_anna_stockcredits3')
         )

        (ml.overlay.Overlay()
            .add_image("image/ui/title/eckannacuredending.png", condition="persistent.eckannacured")
            .compile_to("main_menu")
         )

    @staticmethod
    def mod_complete():
        pass

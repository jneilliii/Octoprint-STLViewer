# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class stlviewer(octoprint.plugin.StartupPlugin,
				octoprint.plugin.TemplatePlugin,
				octoprint.plugin.AssetPlugin):
					   
	def on_after_startup(self):
		self._logger.info("STL Viewer loaded!")

	def get_template_configs(self):
		return []

	def get_assets(self):
		return dict(
			js=["js/stlviewer.js","js/jsc3d.js","js/jsc3d.touch.js"]
		)

	##-- Image upload extenstion tree hook
	def get_extension_tree(self, *args, **kwargs):
		return dict(
			model=dict(
				stlviewer=["stl"]
			)
		)

	##~~ Softwareupdate hook
	def get_update_information(self):
		return dict(
			stlviewer=dict(
				displayName="STL Viewer",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-STLViewer",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-STLViewer/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "STL Viewer"
__plugin_pythoncompat__ = ">=2.7,<4"


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = stlviewer()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.filemanager.extension_tree": __plugin_implementation__.get_extension_tree
	}
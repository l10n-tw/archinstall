from typing import List, Optional, Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class BspwmProfile(XorgProfile):
	def __init__(self):
		super().__init__('Bspwm', ProfileType.WindowMgr, description='')

	@property
	def packages(self) -> List[str]:
		return [
			'dwm',
			'st',
			'dmenu',
			'picom',
			'xorg-xsetroot',
      'xorg-xset',
      'pywal',
      'xdo',
      'dunst',
      'slock'
		]

	@property
	def default_greeter_type(self) -> Optional[GreeterType]:
		return GreeterType.Lightdm

	def preview_text(self) -> Optional[str]:
		text = str(_('Environment type: {}')).format(self.profile_type.value)
		return text + '\n' + self.packages_text()

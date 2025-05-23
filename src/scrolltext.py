import harfang as hg
from math import pi, cos, sin

# demo scroll text

scroll_text = "   "
scroll_text = scroll_text + "                                                                                                       "
scroll_text = scroll_text + "                                                                                                       "
# start

scroll_text = scroll_text + "Welcome folks to this new Music Disk production by Resistance, released for EVOKE 2022 in Koln, Germany."
scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "Idea, graphics, main coding : Fra"
scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "Interaction design : Romboyj"
scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "Composers : Aceman, Erk, GliGli, mAZE, Nainain, Riddlemak, WillBe"
scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "Additionnal coding : Erk"
scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "3D engine : HARFANG"
scroll_text = scroll_text + ", "
scroll_text = scroll_text + "additionnal thanks to Kipixelle, Mooz, Scorpheus, Xbarr for this nice piece of 3D software!"
scroll_text = scroll_text + " "

scroll_text = scroll_text + "   -   "
scroll_text = scroll_text + "Songs/Composers, by order in the playlist: "

scroll_text = scroll_text + "'Elsewhere' by Erk" + ", "
scroll_text = scroll_text + "'Of Lobsters and Men' by Aceman" + ", "
scroll_text = scroll_text + "'Sweet Mermaids' by Nainain" + ", "
scroll_text = scroll_text + "'Coral Pillows' by willBe" + ", "
scroll_text = scroll_text + "'6502 Fathoms' by mAZE" + ", "
scroll_text = scroll_text + "'Mountains City' by Erk" + ", "
scroll_text = scroll_text + "'Underwater' by GliGli" + ", "
scroll_text = scroll_text + "'Electronics Underground' by Erk" + ", "
scroll_text = scroll_text + "'A.I.' by Riddlemak"

scroll_text = scroll_text + "   -   "

scroll_text = scroll_text + "We hope you will enjoy all these nice electro/hiphop tracks... "
scroll_text = scroll_text + "and now let's hand over the keyboard to the team ... "

scroll_text = scroll_text + "   -   "

scroll_text = scroll_text + "Hi there, AceMan on the keys. I am very pleased to be part of this fantastic music disk" 
scroll_text = scroll_text + " - underwater theme is one of my favourite ones out there (I love water levels in games. "
scroll_text = scroll_text + "Yes, I really do!) so when Fra asked me about a tune I instantly knew what I want to do :) "
scroll_text = scroll_text + "As always, it's made 100% in Renoise using only samples and internal FXs, you can grab .xrns file out there. "
scroll_text = scroll_text + "I wish you all a fantastic journey with this music disk, stay safe and wash your pants. Hands. Too."

scroll_text = scroll_text + "  ...  "

scroll_text = scroll_text + "Erk here, greetings would humbly fly to: Silicon, Sly, Tex, Gwen."

scroll_text = scroll_text + "  ...  "

scroll_text = scroll_text + "Willbe sends love bubbles to: Fra, Sigmate, Jeenio, Irokos, Dax, TSR, Patrox, Kaneel, "
scroll_text = scroll_text + "Chaosnet, Moonove, Med, Alkama, Torone, Nytrik, Guille, Ntsc, Splif, Niakool, Jaylee, "
scroll_text = scroll_text + "Shi, Sear, Skal, Heatseeker, Pitbull, Rez, Keops, Smash, XXX, Mali, Kenet, Made, Yes, "
scroll_text = scroll_text + "Chandra, Traven, Mandrixx, Lycan, Nnorm, Xtrium, PS, Shodan, Rakiz, Skyfire, Boub, Stv, "
scroll_text = scroll_text + "Rahow, Flure, Wullon, Flod, Stv, Garbagetruck."

scroll_text = scroll_text + "  ...  "

scroll_text = scroll_text + "Love to our friends, Futuris, Altair, Arise, Agenda, Dreamweb, speccy.pl, Xenium Orga Team, "
scroll_text = scroll_text + "Joker, MultiStyle Labs, Elysium, Genesis Project, OftenHide, GGS, Lamers, CrapTeam, Amnesty, "
scroll_text = scroll_text + "Tristesse, Pixel Nation, Samar, AYCE, Aberration Creations, Elude, Plastic, Floppy, Implexy, "
scroll_text = scroll_text + "Lalka, Nah-Kolor, Suspect, Ghostown, Whelpz, Potion, MAWI, Anadune, Flush, Vital-Motion, Mankind, Mandarine ..."

scroll_text = scroll_text + "  ...  "

scroll_text = scroll_text + "Fra again, let's talk a bit about this music disk :) ... "
scroll_text = scroll_text + "This project started as ... a level for video game. The game was meant to be a space racer, "
scroll_text = scroll_text + "with ultra fast spaceships running accros different circuits. The gameplay was 2D but "
scroll_text = scroll_text + "the display was all in 3D (using a pre-version of the HARFANG engine...)è "
scroll_text = scroll_text + "The idea was to model nice 3D landscapes that would show up in the background of each level. "
scroll_text = scroll_text + "I had a chat with a team and suggested that I could work on some of the background scenes..."
scroll_text = scroll_text + "The game finally never reached the market, but I kept the 3D files... "
scroll_text = scroll_text + "All in all, this 3D scene is a level of a game that never was... "
scroll_text = scroll_text + " "

scroll_text = scroll_text + "The idea to turn this into a music disk came slowly... Nainain had just installed his new music home studio "
scroll_text = scroll_text + "and started to test it on original compositions. He sent me one of his draft themes that was reaaaaally promising "
scroll_text = scroll_text + "and a perfect match to this aquatic 3D scene I had on my harddrive, so we came up with the idea of a tiny demo... "
scroll_text = scroll_text + "But... from this demo idea, I started to ask friends in Resistance and outside "
scroll_text = scroll_text + "if they would be interested in contributing to a music disk. "
scroll_text = scroll_text + "The visual look was already almost completed and I guess it helped to provide some inspiration. "
scroll_text = scroll_text + " "

scroll_text = scroll_text + "On the technical sides of things, this demo is built on the HARFANG 3D engine... "
scroll_text = scroll_text + "What is HARFANG? It's a data-driven 3D engine that can run almost everywhere, "
scroll_text = scroll_text + "as a Python module, as a Golang module, as C++ SDK, or as a Lua extension "
scroll_text = scroll_text + "which is a the case of this demo! "
scroll_text = scroll_text + "It means that all this demo was scripted in Lua, including the interactions "
scroll_text = scroll_text + "and the visual/fx and custom (sort of) rendering pipeline... "
scroll_text = scroll_text + "Come check HARFANG, on www.harfang3d.com, or on Github as it's open source!"
scroll_text = scroll_text + " "

scroll_text = scroll_text + "  ...  "

scroll_text = scroll_text + " "
scroll_text = scroll_text + "This concludes the end of this scrolltext, it will now loop :) ... "


scroll_text = scroll_text + "(press ESC to exit!)"

# end
scroll_text = scroll_text + "                                                                                                       "

# scroll text drawing routine
# on-screen usage text
def update_demo_scroll_text(dt, view_id, res_x, res_y, scroll_x, char_offset, ns, scroll_text, font, font_program, font_size, text_render_state, fade=1.0):
	scroll_char_len = 120
	scroll_x = scroll_x + hg.time_to_sec_f(dt) * 60.0 * 1.5 # math.min(1.0/60.0, hg.time_from_sec_f(dt)) * 60.0

	if scroll_x > ns:
		scroll_x = 0
		char_offset = char_offset + 1
		_r = hg.ComputeTextRect(font, scroll_text[char_offset])
		ns = _r.ex - _r.sx
	# end
	
	text_pos = hg.Vec3(-(16 * res_x) / 1280, res_y - (font_size * 1.25), 0)
	text_pos.x = text_pos.x - scroll_x

	text_sub = scroll_text[char_offset:char_offset + scroll_char_len]

	bold_radius = (5.0 * res_x) / 1280
	for l in range(0, int(bold_radius), 2):
		for a in range(0, 360, 60):
			bold_offset = hg.Vec3(cos(a * pi / 180.0), sin(a * pi / 180.0), 0.0) * bold_radius
			bold_offset.x = bold_offset.x + l
			bold_offset.y = bold_offset.y + l
			hg.DrawText(view_id, font, text_sub, font_program, 'u_tex', 0, hg.Mat4.Identity, text_pos + bold_offset, 
			hg.DTHA_Left, hg.DTVA_Bottom, [hg.MakeUniformSetValue('u_color', hg.Vec4(0, 0.075, 0.1, fade))], [], text_render_state)
	# 	end
	# end
	
	hg.DrawText(view_id, font, text_sub, font_program, 'u_tex', 0, hg.Mat4.Identity, text_pos, hg.DTHA_Left, hg.DTVA_Bottom, [hg.MakeUniformSetValue('u_color', hg.Vec4(0, 0.45, 0.5, fade))], [], text_render_state)

	if char_offset > len(scroll_text):
		char_offset = 0
	# end

	return view_id, scroll_x, char_offset, ns
# end
#
# Leaderboard Config
#
# This config file contains just one constant: LEADERBOARD_CONFIG
# It is used to handle a lot of the leaderboard requirements around
# variable IDs, value IDs and other filtering.
#
# Sometimes, a board may contain sub-boards or sub-categories.
# We handle them here so that they can be detected and processed properly.
#
LEADERBOARD_CONFIG = {
	"hp1_6th_gen": {
		"any": {
			"variables": [
				{"name": "console", "var_id": "9l7ro37n", "value_id": "klr8pkj1"},
				{"name": "emulator", "var_id": "9l7ro37n", "value_id": "21dpz841"},
			]
		},
		"100": {
			"variables": [
				{"name": "console", "var_id": "9l7ro37n", "value_id": "klr8pkj1"},
				{"name": "emulator", "var_id": "9l7ro37n", "value_id": "21dpz841"},
			]
		},
		"nms": {
			"variables": [
				{"name": "console", "var_id": "9l7ro37n", "value_id": "klr8pkj1"},
				{"name": "emulator", "var_id": "9l7ro37n", "value_id": "21dpz841"}
			]
		}
	},
	"hp2_6th_gen": {
		"any": {
			"variables": [
				{"name": "console", "var_id": "kn0vxg0l", "value_id": "5lm72p0l"},
				{"name": "emulator", "var_id": "kn0vxg0l", "value_id": "21dpz841"},
			]
		},
		"100": {
			"variables": [
				{"name": "console", "var_id": "kn0vxg0l", "value_id": "5lm72p0l"},
				{"name": "emulator", "var_id": "kn0vxg0l", "value_id": "21dpz841"},
			]
		},
		"nms": {
			"variables": [
				{"name": "console", "var_id": "kn0vxg0l", "value_id": "5lm72p0l"},
				{"name": "emulator", "var_id": "kn0vxg0l", "value_id": "21dpz841"}
			]
		}
	},
	"hp3_6th_gen": {
		"any": {
			"variables": [
				{"name": "console", "var_id": "yn2wrvjn", "value_id": "5q8n6vgq"},
				{"name": "emulator", "var_id": "yn2wrvjn", "value_id": "4qykp241"},
			]
		},
		"100": {
			"variables": [
				{"name": "console", "var_id": "yn2wrvjn", "value_id": "5q8n6vgq"},
				{"name": "emulator", "var_id": "yn2wrvjn", "value_id": "4qykp241"},
			]
		},
		"nms": {
			"variables": [
				{"name": "console", "var_id": "yn2wrvjn", "value_id": "5q8n6vgq"},
				{"name": "emulator", "var_id": "yn2wrvjn", "value_id": "4qykp241"}
			]
		}
	},
	"hp2_ps2": {
		"any": {
			"variables": [
				{"name": "console", "var_id": "yn20gk2l", "value_id": "139v60r1"},
				{"name": "emulator", "var_id": "yn20gk2l", "value_id": "qvv4y7rq"},
			],
		},
		"100": {
			"variables": [
				{"name": "console", "var_id": "yn20gk2l", "value_id": "139v60r1"},
				{"name": "emulator", "var_id": "yn20gk2l", "value_id": "qvv4y7rq"},
			],
		},
		"noeds": {
			"variables": [
				{"name": "console", "var_id": "yn20gk2l", "value_id": "139v60r1"},
				{"name": "emulator", "var_id": "yn20gk2l", "value_id": "qvv4y7rq"}
			],
		}
	},
	"hp4": {
		"any": {
			"variables": [
				{"name": "1p", "aliases": ["1player"], "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "aliases": ["2players"], "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "aliases": ["3players"], "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		},
		"100": {
			"variables": [
				{"name": "1p", "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		},
		"allshields": {
			"variables": [
				{"name": "1p", "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		}
	},
	"hp4_gba": {
		"any": {
			"variables": [{"var_id": "j84k0x2n", "value_id": "21gjm281"}],
		},
		"100": {
			"variables": [{"var_id": "j84k0x2n", "value_id": "21gjm281"}]
		}
	},
	"hp4_ds": {
		"any": {
			"variables": [
				{"name": "console", "var_id": "j84k0x2n", "value_id": "jqz6jx81"},
				{"name": "emulator", "var_id": "j84k0x2n", "value_id": "rqv8m951"}
			],
		},
		"100": {
			"variables": [
				{"name": "console", "var_id": "j84k0x2n", "value_id": "jqz6jx81"},
				{"name": "emulator", "var_id": "j84k0x2n", "value_id": "rqv8m951"}
			]
		}
	},
	"legacy_pc": {
		"ranrok": {
			"variables": [
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"},
				{"name": "platform", "var_id": "e8mqwzvn", "value_id": "10vomkpl"}
			]
		},
		"any": {
			"variables": [
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"},
				{"name": "platform", "var_id": "e8mqwzvn", "value_id": "10vomkpl"}
			]
		},
		"100": {
			"variables": [
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"},
				{"name": "platform", "var_id": "e8mqwzvn", "value_id": "10vomkpl"}
			]
		},
		"allquests": {
			"variables": [
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"},
				{"name": "platform", "var_id": "e8mqwzvn", "value_id": "10vomkpl"}
			]
		}
	},
	"hpce": {
		"1pc_100gless": {
			"board": "1PC",
			"variables": [
				{"var_id": "789x9o08", "value_id": "9qj95y0l"}
			]
		},
		"1pc_allchests": {
			"board": "1PC",
			"variables": [
				{"var_id": "789x9o08", "value_id": "qj7o0j3q"}
			]
		},
		"1pc_boostless": {
			"board": "1PC",
			"variables": [
				{"var_id": "789x9o08", "value_id": "810prejl"}
			]
		},
		"1pc_highjump": {
			"board": "1PC",
			"variables": [
				{"var_id": "789x9o08", "value_id": "qvv4doyq"}
			]
		},
		"1pc_lowcast": {
			"board": "1PC",
			"variables": [
				{"var_id": "789x9o08", "value_id": "rqvj9v5q"}
			]
		},
		"2pc_100gless": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "013pyekl"}
			]
		},
		"2pc_allchests": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "le23je6l"}
			]
		},
		"2pc_awcgless": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "0q5p0erl"}
			]
		},
		"2pc_boostless": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "5lmp9jyl"}
			]
		},
		"2pc_chungus": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "rqv2jkw1"}
			]
		},
		"2pc_cutscene": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "rqv9nw5l"}
			]
		},
		"2pc_hpwc": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "4lx9jwjl"}
			]
		},
		"2pc_highjump": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "xqkpp04l"}
			]
		},
		"2pc_jumpless": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "qyzx9721"}
			]
		},
		"2pc_lowcast": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "814pnew1"}
			]
		},
		"2pc_ng": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "81w9kw9l"}
			]
		},
		"2pc_nmg": {
			"board": "2PC",
			"variables": [
				{"var_id": "2lg3d4on", "value_id": "zqo97wgq"}
			]
		},
		"3pc_any": {
			"board": "3PC",
			"variables": [
				{"var_id": "02qwx172", "value_id": "014g7x21"}
			]
		},
		"4pc_avc_1p": {
			"board": "4PC",
			"variables": [
				{"name": "board_id", "var_id": "5ly156yl", "value_id": "0q5p0zrl"},
				{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "14oy0mkq"}
			]
		},
		"4pc_avc_2p": {
			"board": "4PC",
			"variables": [
				{"name": "board_id", "var_id": "5ly156yl", "value_id": "0q5p0zrl"},
				{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "192moe4q"}
			]
		},
		"4pc_avc_3p": {
			"board": "4PC",
			"variables": [
				{"name": "board_id", "var_id": "5ly156yl", "value_id": "0q5p0zrl"},
				{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "12vdyj2q"}
			]
		},
		"5pc_amg": {
			"board": "5PC",
			"variables": [
				{"var_id": "rn1zmxpl", "value_id": "5q8pm8rl"}
			]
		},
		"5pc_allportraits": {
			"board": "5PC",
			"variables": [
				{"var_id": "rn1zmxpl", "value_id": "4qy96o3l"}
			]
		},
		"5pc_allsymbols": {
			"board": "5PC",
			"variables": [
				{"var_id": "rn1zmxpl", "value_id": "1dkow2jl"}
			]
		},
		"5pc_chess": {
			"board": "5PC",
			"variables": [
				{"var_id": "rn1zmxpl", "value_id": "mln92m6q"}
			]
		},
		"6pc_pr": {
			"board": "6PC",
			"variables": [
				{"var_id": "gnx606jn", "value_id": "12v2om4q"}
			]
		},
		"1ps1_awc": {
			"board": "1PS1",
			"variables": [
				{"var_id": "jlzx03x8", "value_id": "xqkxnyd1"}
			]
		},
		"1ps1_ss": {
			"board": "1PS1",
			"variables": [
				{"var_id": "jlzx03x8", "value_id": "gq76xmpl"}
			]
		},
		"1ps1_ng": {
			"board": "1PS1",
			"variables": [
				{"var_id": "jlzx03x8", "value_id": "21g3pz6q"}
			]
		},
		"2ps1_awc": {
			"board": "2PS1",
			"variables": [
				{"var_id": "yn23geel", "value_id": "q8kk0p6q"}
			]
		},
		"2ps1_ss": {
			"board": "2PS1",
			"variables": [
				{"var_id": "yn23geel", "value_id": "qoxkedgq"}
			]
		},
		"4psp_any": {
			"board": "4PSP",
			"variables": [
				{"var_id": "38de521n", "value_id": "qyzzymd1"}
			]
		},
		"4psp_100": {
			"board": "4PSP",
			"variables": [
				{"var_id": "38de521n", "value_id": "ln8807nl"}
			]
		},
		"5psp_any": {
			"board": "5PSP",
			"variables": [
				{"var_id": "r8rewy2l", "value_id": "q655xwol"}
			]
		},
		"5psp_100": {
			"board": "5PSP",
			"variables": [
				{"var_id": "r8rewy2l", "value_id": "lmoo4e01"}
			]
		},
		"mr_glessduo": {
			"board": "Multiruns",
			"variables": [
				{"var_id": "p85rz75n", "value_id": "810prjjl"}
			]
		},
		"mr_rpgtri": {
			"board": "Multiruns",
			"variables": [
				{"var_id": "p85rz75n", "value_id": "9qj95n0l"}
			]
		},
		"insane_hp1_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "21d7dm41"}
			]
		},
		"insane_hp2_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "klrw7rj1"}
			]
		},
		"insane_hp3_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "5q87zmgl"}
			]
		},
		"insane_hp4_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "5lezyezl"}
			]
		},
		"insane_hp5_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "0q5zw2nq"}
			]
		},
		"insane_hp6_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "4lxo2yrl"}
			]
		},
		"insane_hp71_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "814gm2j1"}
			]
		},
		"insane_hp72_pc": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "z19yezkl"}
			]
		},
		"insane_1ps1": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "4qyd206q"}
			]
		},
		"insane_2ps1": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "mlnpvxo1"}
			]
		},
		"insane_hp2_6th_gen": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "013z2zyq"}
			]
		},
		"insane_hp3_6th_gen": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "5lm0z3j1"}
			]
		},
		"insane_hp1_gba": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "jq663o3q"}
			]
		},
		"insane_hp2_gba": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "q75dkjd1"}
			]
		},
		"insane_hp3_gba": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "rqv025rl"}
			]
		},
		"insane_qwc_gba": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "q654y2nl"}
			]
		},
		"insane_hp6_ds": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "zqovk7g1"}
			]
		},
		"insane_hp71_ds": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "1py422g1"}
			]
		},
		"insane_hp72_ds": {
			"board": "Insane%",
			"variables": [
				{"var_id": "7896d298", "value_id": "klrg73oq"}
			]
		},
		"sy_hp1_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "4qye4641"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp2_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "mln6320q"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp3_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "810e7rwq"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp4_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "9qjyd5eq"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp5_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "jq6k7j3l"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp6_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "5lmjn9jl"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp71_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "81ww8ko1"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]
		},
		"sy_hp72_any": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "zqown7pl"},
				{"var_id": "wl30dmyl", "value_id": "013erydq"}
			]

		},
		"sy_hp1_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "4qye4641"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp2_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "mln6320q"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp3_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "810e7rwq"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp4_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "9qjyd5eq"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp5_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "jq6k7j3l"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp6_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "5lmjn9jl"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp71_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "81ww8ko1"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"sy_hp72_100": {
			"board": "Single Year",
			"variables": [
				{"var_id": "2lgr1v7n", "value_id": "zqown7pl"},
				{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
			]
		},
		"dvd_hc": {
			"board": "DVD Games",
			"variables": [
				{"var_id": "r8r7v77n", "value_id": "jqzd3e4l"}
			]
		},
		"dvd_ww": {
			"board": "DVD Games",
			"variables": [
				{"var_id": "r8r7v77n", "value_id": "klrm240q"}
			]
		}
	},
	"hpmulti": {
		"pctri_any": {
			"board": "PC Trifecta",
			"variables": [
				{"var_id": "0nw0e0kl", "value_id": "p12099kl"}
			]
		},
		"pctri_100": {
			"board": "PC Trifecta",
			"variables": [
				{"var_id": "0nw0e0kl", "value_id": "81p5eekl"}
			]
		},
		"pctri_awc": {
			"board": "PC Trifecta",
			"variables": [
				{"var_id": "0nw0e0kl", "value_id": "p120927l"}
			]
		},
		"pcocto_any": {
			"board": "PC Octofecta",
			"variables": [
				{"var_id": "wl3dqd98", "value_id": "klr2xx21"}
			]
		},
		"pcocto_100": {
			"board": "PC Octofecta",
			"variables": [
				{"var_id": "wl3dqd98", "value_id": "21de6vjl"}
			]
		},
		"7pcduo_any": {
			"board": "7PC Duofecta",
			"variables": [
				{"var_id": "789dqd6n", "value_id": "xqknooyq"}
			]
		},
		"7pcduo_100": {
			"board": "7PC Duofecta",
			"variables": [
				{"var_id": "789dqd6n", "value_id": "gq7x22yl"}
			]
		},
		"ps1duo_any": {
			"board": "PS1 Duofecta",
			"variables": [
				{"var_id": "wlek5kkl", "value_id": "5q8942k1"}
			]
		},
		"ps1duo_100": {
			"board": "PS1 Duofecta",
			"variables": [
				{"var_id": "wlek5kkl", "value_id": "4qyw7571"}
			]
		},
		"ps1duo_nms": {
			"board": "PS1 Duofecta",
			"variables": [
				{"var_id": "wlek5kkl", "value_id": "p120957l"}
			]
		},
		"6thgentri_any": {
			"board": "6th Gen Trifecta",
			"variables": [
				{"var_id": "68k737yl", "value_id": "mlnoeddq"}
			]
		},
		"6thgentri_100": {
			"board": "6th Gen Trifecta",
			"variables": [
				{"var_id": "68k737yl", "value_id": "9qj82wg1"}
			]
		},
		"gbcduo_any": {
			"board": "GBC Duofecta",
			"variables": [
				{"var_id": "j84d0dj8", "value_id": "jq6evy7l"}
			]
		},
		"gbcduo_100": {
			"board": "GBC Duofecta",
			"variables": [
				{"var_id": "j84d0dj8", "value_id": "5lmm284l"}
			]
		},
		"gbapenta_any": {
			"board": "GBA Pentafecta",
			"variables": [
				{"var_id": "rn1jqjkn", "value_id": "81w07e5l"}
			]
		},
		"gbapenta_100": {
			"board": "GBA Pentafecta",
			"variables": [
				{"var_id": "rn1jqjkn", "value_id": "zqovjm21"}
			]
		},
		"hhocto_any": {
			"board": "Handheld Octofecta",
			"variables": [
				{"var_id": "p855j508", "value_id": "0136xw31"}
			]
		},
		"hhocto_100": {
			"board": "Handheld Octofecta",
			"variables": [
				{"var_id": "p855j508", "value_id": "rqvyx6wq"}
			]
		},
		"fs_any": {
			"board": "Full Series",
			"variables": [
				{"var_id": "38dm1m18", "value_id": "5lexn3zq"}
			]
		},
		"fs_100": {
			"board": "Full Series",
			"variables": [
				{"var_id": "38dm1m18", "value_id": "0q534xn1"}
			]
		}
	},
	"hp14": {
		"any_solo_nocut": {
			"board": "1PC",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "p85dm5xl", "value_id": "jq68d97l"}
			]
		},
		"any_coop_nocut": {
			"board": "Any%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "p85dm5xl", "value_id": "jq68d97l"}
			]
		},
		"any_solo_standard": {
			"board": "Any%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "p85dm5xl", "value_id": "mlngx4d1"}
			]
		},
		"any_coop_standard": {
			"board": "Any%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "p85dm5xl", "value_id": "mlngx4d1"}
			]
		},
		"nle_solo_nocut": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "p8554jx8", "value_id": "gq78jvn1"}
			]
		},
		"nle_solo_standard": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "kn03d0n3"},
				{"var_id": "p8554jx8", "value_id": "xqkvjg9l"}
			]
		},
		"nle_coop_nocut": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "p8554jx8", "value_id": "gq78jvn1"}
			]
		},
		"nle_coop_standard": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "p8554jx8", "value_id": "xqkvjg9l"}
			]
		},
		"freeplay_solo": {
			"board": "Free Play",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"}
			]
		},
		"freeplay_coop": {
			"board": "Free Play",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"}
			]
		},
		"replay_solo": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"}
			]
		},
		"replay_coop": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"}
			]
		},
		"ac_solo_nocut": {
			"board": "All Crests",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "38dwxmxn", "value_id": "5lm75r4l"}
			]
		},
		"ac_solo_standard": {
			"board": "All Crests",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "38dwxmxn", "value_id": "81024o5q"}
			]
		},
		"ac_coop_nocut": {
			"board": "All Crests",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "38dwxmxn", "value_id": "5lm75r4l"}
			]
		},
		"ac_coop_standard": {
			"board": "All Crests",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "38dwxmxn", "value_id": "81024o5q"}
			]
		},
		"100_solo_nocut": {
			"board": "100%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "r8rqjewl", "value_id": "81w6yv5l"}
			]
		},
		"100_solo_standard": {
			"board": "100%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "xqkek0nq"},
				{"var_id": "r8rqjewl", "value_id": "9qjp36gq"}
			]
		},
		"100_coop_nocut": {
			"board": "100%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "r8rqjewl", "value_id": "81w6yv5l"}
			]
		},
		"100_coop_standard": {
			"board": "100%",
			"variables": [
				{"var_id": "kn03d0n3", "value_id": "gq75ejv1"},
				{"var_id": "r8rqjewl", "value_id": "9qjp36gq"}
			]
		}
	},
	"hp57": {
		"any_solo_nocut_unrestricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "dlorq6rl", "value_id": "mlngg2d1"}
			]
		},
		"any_solo_standard_unrestricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "dlorq6rl", "value_id": "4qykk671"}
			]
		},
		"any_coop_nocut_unrestricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "dlorq6rl", "value_id": "mlngg2d1"}
			]
		},
		"any_coop_standard_unrestricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "dlorq6rl", "value_id": "4qykk671"}
			]
		},
		"any_solo_nocut_restricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "dlorq6rl", "value_id": "mlngg2d1"}
			]
		},
		"any_solo_standard_restricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "dlorq6rl", "value_id": "4qykk671"}
			]
		},
		"any_coop_nocut_restricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "dlorq6rl", "value_id": "mlngg2d1"}
			]
		},
		"any_coop_standard_restricted": {
			"board": "Any%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "dlorq6rl", "value_id": "4qykk671"}
			]
		},
		"nle_solo_nocut_unrestricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p85jw5lg"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "jlzgmxxn", "value_id": "9qjpp5gq"}
			]
		},
		"nle_solo_standard_unrestricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p85jw5lg"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "jlzgmxxn", "value_id": "81022r5q"}
			]
		},
		"nle_coop_nocut_unrestricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p85jw5lg"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "jlzgmxxn", "value_id": "9qjpp5gq"}
			]
		},
		"nle_coop_standard_unrestricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p85jw5lg"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "jlzgmxxn", "value_id": "81022r5q"}
			]
		},
		"nle_solo_nocut_restricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "jlzgmxxn", "value_id": "9qjpp5gq"}
			]
		},
		"nle_solo_standard_restricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "jlzgmxxn", "value_id": "81022r5q"}
			]
		},
		"nle_coop_nocut_restricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "jlzgmxxn", "value_id": "9qjpp5gq"}
			]
		},
		"nle_coop_standard_restricted": {
			"board": "No Levels Early",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "jlzgmxxn", "value_id": "81022r5q"}
			]
		},
		"freeplay_solo_unrestricted": {
			"board": "Free Play",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
			],
		},
		"freeplay_coop_unrestricted": {
			"board": "Free Play",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
			],
		},
		"freeplay_solo_restricted": {
			"board": "Free Play",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
			],
		},
		"freeplay_coop_restricted": {
			"board": "Free Play",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
			],
		},
		"replay_solo_unrestricted": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
			],
		},
		"replay_coop_unrestricted": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
			],
		},
		"replay_solo_restricted": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
			],
		},
		"replay_coop_restricted": {
			"board": "Replay Story",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
			],
		},
		"ac_solo_nocut_unrestricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "9l7rz59n", "value_id": "5lm7794l"}
			]
		},
		"ac_solo_standard_unrestricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "9l7rz59n", "value_id": "jq688j7l"}
			]
		},
		"ac_coop_nocut_unrestricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "9l7rz59n", "value_id": "5lm7794l"}
			]
		},
		"ac_coop_standard_unrestricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "9l7rz59n", "value_id": "jq688j7l"}
			]
		},
		"ac_solo_nocut_restricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "9l7rz59n", "value_id": "5lm7794l"}
			]
		},
		"ac_solo_standard_restricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "9l7rz59n", "value_id": "jq688j7l"}
			]
		},
		"ac_coop_nocut_restricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "9l7rz59n", "value_id": "5lm7794l"}
			]
		},
		"ac_coop_standard_restricted": {
			"board": "All Crests",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "9l7rz59n", "value_id": "jq688j7l"}
			]
		},
		"100_solo_nocut_unrestricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "yn2w4m0n", "value_id": "zqozz72l"}
			]
		},
		"100_solo_standard_unrestricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "yn2w4m0n", "value_id": "81w66k5l"}
			]
		},
		"100_coop_nocut_unrestricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "yn2w4m0n", "value_id": "zqozz72l"}
			]
		},
		"100_coop_standard_unrestricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "p12867d1"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "yn2w4m0n", "value_id": "81w66k5l"}
			]
		},
		"100_solo_nocut_restricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "yn2w4m0n", "value_id": "zqozz72l"}
			]
		},
		"100_solo_standard_restricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "4qyzp371"},
				{"var_id": "yn2w4m0n", "value_id": "81w66k5l"}
			]
		},
		"100_coop_nocut_restricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "yn2w4m0n", "value_id": "zqozz72l"}
			]
		},
		"100_coop_standard_restricted": {
			"board": "100%",
			"variables": [
				{"var_id": "38dmm4z8", "value_id": "z19wjnyq"},
				{"var_id": "p85jw5lg", "value_id": "mln8wrdl"},
				{"var_id": "yn2w4m0n", "value_id": "81w66k5l"}
			]
		}
	}
}

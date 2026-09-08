#
# Leaderboard Config
#
# This config file contains just one constant: LEADERBOARD_CONFIG
# It is used to handle a lot of the leaderboard requirements around
# variable IDs, value IDs and other filtering.
#
# Sometimes, a board may contain sub-boards or sub-categories.
# We handle them here so that they can be detected and processed properly.
# The aliases sub-key may be required if you have troubles calling for
# PBs with the !pb command.
#
LEADERBOARD_CONFIG = {
	"hp1_6th_gen": {
		"categories": {
			"any": {
				"variables": [
					{"name": "console", "var_id": "zd3yw82n-9l7ro37n", "value_id": "klr8pkj1"},
					{"name": "emulator", "var_id": "zd3yw82n-9l7ro37n", "value_id": "21dpz841"},
				]
			},
			"100": {
				"variables": [
					{"name": "console", "var_id": "9d839vw2-9l7ro37n", "value_id": "klr8pkj1"},
					{"name": "emulator", "var_id": "9d839vw2-9l7ro37n", "value_id": "21dpz841"},
				]
			},
			"nms": {
				"variables": [
					{"name": "console", "var_id": "zdnlom72-9l7ro37n", "value_id": "klr8pkj1"},
					{"name": "emulator", "var_id": "zdnlom72-9l7ro37n", "value_id": "21dpz841"}
				]
			}
		}
	},
	"hp2_6th_gen": {
		"categories": {
			"any": {
				"variables": [
					{"name": "console", "var_id": "824x9wgd-kn0vxg0l", "value_id": "5lm72p0l"},
					{"name": "emulator", "var_id": "824x9wgd-kn0vxg0l", "value_id": "21dpz841"},
				]
			},
			"100": {
				"variables": [
					{"name": "console", "var_id": "9d8pnr3k-kn0vxg0l", "value_id": "5lm72p0l"},
					{"name": "emulator", "var_id": "9d8pnr3k-kn0vxg0l", "value_id": "21dpz841"},
				]
			},
			"nms": {
				"variables": [
					{"name": "console", "var_id": "mkelyo9d-kn0vxg0l", "value_id": "5lm72p0l"},
					{"name": "emulator", "var_id": "mkelyo9d-kn0vxg0l", "value_id": "21dpz841"}
				]
			}
		}
	},
	"hp3_6th_gen": {
		"categories": {
			"any": {
				"variables": [
					{"name": "console", "var_id": "wdmqx52q-yn2wrvjn", "value_id": "5q8n6vgq"},
					{"name": "emulator", "var_id": "wdmqx52q-yn2wrvjn", "value_id": "4qykp241"},
				]
			},
			"100": {
				"variables": [
					{"name": "console", "var_id": "mkerv6nd-yn2wrvjn", "value_id": "5q8n6vgq"},
					{"name": "emulator", "var_id": "mkerv6nd-yn2wrvjn", "value_id": "4qykp241"},
				]
			},
			"nms": {
				"variables": [
					{"name": "console", "var_id": "xk9el1x2-yn2wrvjn", "value_id": "5q8n6vgq"},
					{"name": "emulator", "var_id": "xk9el1x2-yn2wrvjn", "value_id": "4qykp241"}
				]
			}
		}
	},
	"hp2_ps2": {
		"categories": {
			"any": {
				"variables": [
					{"name": "console", "var_id": "rklo0owk-yn20gk2l", "value_id": "139v60r1"},
					{"name": "emulator", "var_id": "rklo0owk-yn20gk2l", "value_id": "qvv4y7rq"},
				],
			},
			"100": {
				"variables": [
					{"name": "console", "var_id": "ndxvrvj2-yn20gk2l", "value_id": "139v60r1"},
					{"name": "emulator", "var_id": "ndxvrvj2-yn20gk2l", "value_id": "qvv4y7rq"},
				],
			},
			"noeds": {
				"variables": [
					{"name": "console", "var_id": "w209e9z2-yn20gk2l", "value_id": "139v60r1"},
					{"name": "emulator", "var_id": "w209e9z2-yn20gk2l", "value_id": "qvv4y7rq"}
				],
			}
		}
	},
	"hpce": {
		"aliases": {
			"1PC": ["1pc", "hp1pc"],
			"2PC": ["2pc", "hp2pc"],
			"3PC": ["3pc", "hp3pc"],
			"4PC": ["4pc", "hp4pc"],
			"5PC": ["5pc", "hp5pc"],
			"6PC": ["6pc", "hp6pc"],
			"Single Year": ["sy", "singleyear"],
			"Insane%": ["insane", "ins"],
			"Multiruns": ["mr", "hpmr", "multiruns", "hpmultiruns"],
			"1PS1": ["1ps1", "hp1ps1"],
			"2PS1": ["2ps1", "hp2ps1"],
			"4PSP": ["4psp", "hp4psp"],
			"5PSP": ["5psp", "hp5psp"],
			"DVD Games": ["dvd", "dvdgames", "hpdvdgames"]
		},
		"categories": {
			"1pc_100gless": {
				"board": "1PC",
				"subcategory": "100-glitchless",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "9qj95y0l"}
				]
			},
			"1pc_allchests": {
				"board": "1PC",
				"subcategory": "all-chests",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "qj7o0j3q"}
				]
			},
			"1pc_boostless": {
				"board": "1PC",
				"subcategory": "boostless",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "810prejl"}
				]
			},
			"1pc_highjump": {
				"board": "1PC",
				"subcategory": "high-jump",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "qvv4doyq"}
				]
			},
			"1pc_lowcast": {
				"board": "1PC",
				"subcategory": "lowcast",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "rqvj9v5q"}
				]
			},
			"2pc_100gless": {
				"board": "2PC",
				"subcategory": "100-glitchless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "013pyekl"}
				]
			},
			"2pc_allchests": {
				"board": "2PC",
				"subcategory": "all-chests",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "le23je6l"}
				]
			},
			"2pc_awcgless": {
				"board": "2PC",
				"subcategory": "awc-glitchless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "0q5p0erl"}
				]
			},
			"2pc_boostless": {
				"board": "2PC",
				"subcategory": "boostless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "5lmp9jyl"}
				]
			},
			"2pc_chungus": {
				"board": "2PC",
				"subcategory": "chungus",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "rqv2jkw1"}
				]
			},
			"2pc_cutscene": {
				"board": "2PC",
				"subcategory": "cutscene",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "rqv9nw5l"}
				]
			},
			"2pc_hpwc": {
				"board": "2PC",
				"subcategory": "harry-potter-wizard-card",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "4lx9jwjl"}
				]
			},
			"2pc_highjump": {
				"board": "2PC",
				"subcategory": "blah",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "xqkpp04l"}
				]
			},
			"2pc_jumpless": {
				"board": "2PC",
				"subcategory": "jumpless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "qyzx9721"}
				]
			},
			"2pc_lowcast": {
				"board": "2PC",
				"subcategory": "lowcast",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "814pnew1"}
				]
			},
			"2pc_ng": {
				"board": "2PC",
				"subcategory": "ng",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "81w9kw9l"}
				]
			},
			"2pc_nmg": {
				"board": "2PC",
				"subcategory": "nmg",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "zqo97wgq"}
				]
			},
			"3pc_any": {
				"board": "3PC",
				"subcategory": "any",
				"variables": [
					{"var_id": "rn1zmxpl-02qwx172", "value_id": "014g7x21"}
				]
			},
			"4pc_avc_1p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-1-Player",
				"variables": [
					{"name": "board_id", "var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "14oy0mkq"}
				]
			},
			"4pc_avc_2p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-2-Players",
				"variables": [
					{"name": "board_id", "var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "192moe4q"}
				]
			},
			"4pc_avc_3p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-3-Players",
				"variables": [
					{"name": "board_id", "var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"name": "player_count", "var_id": "2lgk0jo8", "value_id": "12vdyj2q"}
				]
			},
			"5pc_amg": {
				"board": "5PC",
				"subcategory": "all-minigames",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "5q8pm8rl"}
				]
			},
			"5pc_allportraits": {
				"board": "5PC",
				"subcategory": "all-portraits",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "4qy96o3l"}
				]
			},
			"5pc_allsymbols": {
				"board": "5PC",
				"subcategory": "all-symbols",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "1dkow2jl"}
				]
			},
			"5pc_chess": {
				"board": "5PC",
				"subcategory": "chess",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "mln92m6q"}
				]
			},
			"6pc_pr": {
				"board": "6PC",
				"subcategory": "potions-rush",
				"variables": [
					{"var_id": "z27zyz4k-gnx606jn", "value_id": "12v2om4q"}
				]
			},
			"1ps1_awc": {
				"board": "1PS1",
				"subcategory": "all-wizard-cards",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "xqkxnyd1"}
				]
			},
			"1ps1_ss": {
				"board": "1PS1",
				"subcategory": "superspeed",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "gq76xmpl"}
				]
			},
			"1ps1_ng": {
				"board": "1PS1",
				"subcategory": "ng",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "21g3pz6q"}
				]
			},
			"2ps1_awc": {
				"board": "2PS1",
				"subcategory": "all-wizard-cards",
				"variables": [
					{"var_id": "02qwx172-yn23geel", "value_id": "q8kk0p6q"}
				]
			},
			"2ps1_ss": {
				"board": "2PS1",
				"subcategory": "superspeed",
				"variables": [
					{"var_id": "02qwx172-yn23geel", "value_id": "qoxkedgq"}
				]
			},
			"4psp_any": {
				"board": "4PSP",
				"subcategory": "any",
				"variables": [
					{"var_id": "9kv3g402-38de521n", "value_id": "qyzzymd1"}
				]
			},
			"4psp_100": {
				"board": "4PSP",
				"subcategory": "100",
				"variables": [
					{"var_id": "9kv3g402-38de521n", "value_id": "ln8807nl"}
				]
			},
			"5psp_any": {
				"board": "5PSP",
				"subcategory": "any",
				"variables": [
					{"var_id": "rklm84wd-r8rewy2l", "value_id": "q655xwol"}
				]
			},
			"5psp_100": {
				"board": "5PSP",
				"subcategory": "100",
				"variables": [
					{"var_id": "rklm84wd-r8rewy2l", "value_id": "lmoo4e01"}
				]
			},
			"mr_glessduo": {
				"board": "Multiruns",
				"subcategory": "pc-glitchless-duofecta",
				"variables": [
					{"var_id": "ndx314vd-p85rz75n", "value_id": "810prjjl"}
				]
			},
			"mr_rpgtri": {
				"board": "Multiruns",
				"subcategory": "rpg-trifecta",
				"variables": [
					{"var_id": "ndx314vd-p85rz75n", "value_id": "9qj95n0l"}
				]
			},
			"insane_hp1_pc": {
				"board": "Insane%",
				"subcategory": "hp1-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "21d7dm41"}
				]
			},
			"insane_hp2_pc": {
				"board": "Insane%",
				"subcategory": "hp2-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "klrw7rj1"}
				]
			},
			"insane_hp3_pc": {
				"board": "Insane%",
				"subcategory": "hp3-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5q87zmgl"}
				]
			},
			"insane_hp4_pc": {
				"board": "Insane%",
				"subcategory": "hp4-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5lezyezl"}
				]
			},
			"insane_hp5_pc": {
				"board": "Insane%",
				"subcategory": "hp5-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "0q5zw2nq"}
				]
			},
			"insane_hp6_pc": {
				"board": "Insane%",
				"subcategory": "hp6-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "4lxo2yrl"}
				]
			},
			"insane_hp71_pc": {
				"board": "Insane%",
				"subcategory": "hp7-1-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "814gm2j1"}
				]
			},
			"insane_hp72_pc": {
				"board": "Insane%",
				"subcategory": "hp7-2-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "z19yezkl"}
				]
			},
			"insane_1ps1": {
				"board": "Insane%",
				"subcategory": "hp1-ps1",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "4qyd206q"}
				]
			},
			"insane_2ps1": {
				"board": "Insane%",
				"subcategory": "hp2-ps1",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "mlnpvxo1"}
				]
			},
			"insane_hp2_6th_gen": {
				"board": "Insane%",
				"subcategory": "hp2-gcn-xbox",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "013z2zyq"}
				]
			},
			"insane_hp3_6th_gen": {
				"board": "Insane%",
				"subcategory": "hp3-6th-gen",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5lm0z3j1"}
				]
			},
			"insane_hp1_gba": {
				"board": "Insane%",
				"subcategory": "hp1-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "jq663o3q"}
				]
			},
			"insane_hp2_gba": {
				"board": "Insane%",
				"subcategory": "hp2-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "q75dkjd1"}
				]
			},
			"insane_hp3_gba": {
				"board": "Insane%",
				"subcategory": "hp3-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "rqv025rl"}
				]
			},
			"insane_qwc_gba": {
				"board": "Insane%",
				"subcategory": "qwc-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "q654y2nl"}
				]
			},
			"insane_hp6_ds": {
				"board": "Insane%",
				"subcategory": "hp6-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "zqovk7g1"}
				]
			},
			"insane_hp71_ds": {
				"board": "Insane%",
				"subcategory": "hp7-1-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "1py422g1"}
				]
			},
			"insane_hp72_ds": {
				"board": "Insane%",
				"subcategory": "hp7-2-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "klrg73oq"}
				]
			},
			"sy_hp1_any": {
				"board": "Single Year",
				"subcategory": "hp1-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "4qye4641"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp2_any": {
				"board": "Single Year",
				"subcategory": "hp2-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "mln6320q"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp3_any": {
				"board": "Single Year",
				"subcategory": "hp3-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "810e7rwq"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp4_any": {
				"board": "Single Year",
				"subcategory": "hp4-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "9qjyd5eq"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp5_any": {
				"board": "Single Year",
				"subcategory": "hp5-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "jq6k7j3l"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp6_any": {
				"board": "Single Year",
				"subcategory": "hp6-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "5lmjn9jl"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp71_any": {
				"board": "Single Year",
				"subcategory": "hp7-1-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "81ww8ko1"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp72_any": {
				"board": "Single Year",
				"subcategory": "hp7-2-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "zqown7pl"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]

			},
			"sy_hp1_100": {
				"board": "Single Year",
				"subcategory": "hp1-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "4qye4641"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp2_100": {
				"board": "Single Year",
				"subcategory": "hp2-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "mln6320q"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp3_100": {
				"board": "Single Year",
				"subcategory": "hp3-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "810e7rwq"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp4_100": {
				"board": "Single Year",
				"subcategory": "hp4-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "9qjyd5eq"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp5_100": {
				"board": "Single Year",
				"subcategory": "hp5-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "jq6k7j3l"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp6_100": {
				"board": "Single Year",
				"subcategory": "hp6-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "5lmjn9jl"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp71_100": {
				"board": "Single Year",
				"subcategory": "hp7-1-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "81ww8ko1"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp72_100": {
				"board": "Single Year",
				"subcategory": "hp7-2-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "zqown7pl"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"dvd_hc": {
				"board": "DVD Games",
				"subcategory": "hogwarts-challenge",
				"variables": [
					{"var_id": "jdr966xd-r8r7v77n", "value_id": "jqzd3e4l"}
				]
			},
			"dvd_ww": {
				"board": "DVD Games",
				"subcategory": "wizarding-world",
				"variables": [
					{"var_id": "jdr966xd-r8r7v77n", "value_id": "klrm240q"}
				]
			}
		},
	},
	"hpmulti": {
		"aliases": {
			"PC Trifecta": ["pctri", "pctrifecta"],
			"7PC Duofecta": ["7pcduo", "7pcduofecta"],
			"PS1 Duofecta": ["ps1duo", "ps1duofecta"],
			"PC Octofecta": ["pcocto", "pcoctofecta"],
			"6th Gen Trifecta": ["6thgentri", "6thgentrifecta", "gcntri", "gcntrifecta", "xboxtri", "xboxtrifecta", "ps2tri", "ps2trifecta"]
		},
		"categories": {
			"pctri_any": {
				"board": "PC Trifecta",
				"subcategory": "any",
				"variables": [
					{"var_id": "n2y39y1d-0nw0e0kl", "value_id": "p12099kl"}
				]
			},
			"pctri_100": {
				"board": "PC Trifecta",
				"subcategory": "100",
				"variables": [
					{"var_id": "n2y39y1d-0nw0e0kl", "value_id": "81p5eekl"}
				]
			},
			"pctri_awc": {
				"board": "PC Trifecta",
				"subcategory": "AWC",
				"variables": [
					{"var_id": "n2y39y1d-0nw0e0kl", "value_id": "p120927l"}
				]
			},
			"pcocto_any": {
				"board": "PC Octofecta",
				"subcategory": "any",
				"variables": [
					{"var_id": "n2y39y1d-wl3dqd98", "value_id": "klr2xx21"}
				]
			},
			"pcocto_100": {
				"board": "PC Octofecta",
				"subcategory": "100",
				"variables": [
					{"var_id": "n2y39y1d-wl3dqd98", "value_id": "21de6vjl"}
				]
			},
			"7pc_duofecta_any": {
				"var_id": "789dqd6n",
				"value": "xqknooyq",
				"h": "7PC_Duofecta-Any"
			},
			"7pc_duofecta_100": {
				"var_id": "789dqd6n",
				"value": "gq7x22yl",
				"h": "7PC_Duofecta-100"
			},
			"ps1_duofecta_any": {
				"var_id": "wlek5kkl",
				"value": "5q8942k1",
				"h": "PS1_Duofecta-Any"
			},
			"ps1_duofecta_100": {
				"var_id": "wlek5kkl",
				"value": "4qyw7571",
				"h": "PS1_Duofecta-100"
			},
			"ps1_duofecta_nms": {
				"var_id": "wlek5kkl",
				"value": "p120957l",
				"h": "PS1_Duofecta-NMS"
			},
			"6th_gen_trifecta_any": {
				"var_id": "68k737yl",
				"value": "mlnoeddq",
				"h": "6th_Gen_Trifecta-Any"
			},
			"6th_gen_trifecta_1001": {
				"var_id": "68k737yl",
				"value": "9qj82wg1",
				"h": "6th_Gen_Trifecta-1001"
			},
			"full_series_any": {
				"var_id": "38dm1m18",
				"value": "5lexn3zq",
				"h": "Full_Series-Any"
			},
			"full_series_100": {
				"var_id": "38dm1m18",
				"value": "0q534xn1",
				"h": "Full_Series-100"
			},
			"gbc_duofecta_any": {
				"var_id": "j84d0dj8",
				"value": "jq6evy7l",
				"h": "GBC_Duofecta-Any"
			},
			"gbc_duofecta_100": {
				"var_id": "j84d0dj8",
				"value": "5lmm284l",
				"h": "GBC_Duofecta-100"
			},
			"gba_pentafecta_any": {
				"var_id": "rn1jqjkn",
				"value": "81w07e5l",
				"h": "GBA_Pentafecta-Any"
			},
			"gba_pentafecta_100": {
				"var_id": "rn1jqjkn",
				"value": "zqovjm21",
				"h": "GBA_Pentafecta-100"
			},
			"handheld_octofecta_any": {
				"var_id": "p855j508",
				"value": "0136xw31",
				"h": "Handheld_Octofecta-Any"
			},
			"handheld_octofecta_100": {
				"var_id": "p855j508",
				"value": "rqvyx6wq",
				"h": "Handheld_Octofecta-100"
			}
		}
	}
}
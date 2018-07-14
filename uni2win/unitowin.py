# -*- coding: utf-8 -*-
import re


def replace(input):

	output = input

	output = output.replace(u'\u1000', u'\u0075')#kk
	output = re.sub(u'\u1001', u'\u0063', output)#ka_kway
	output = output.replace(u'\u1002', u'\u002A')#gn
	output = re.sub(u'\u1003', u'\u0043', output)#gg
	output = re.sub(u'\u1004', u'\u0069', output)#nga
	output = re.sub(u'\u1005', u'\u0070', output)#slone
	output = re.sub(u'\u1006', u'\u0071', output)#slane
	output = re.sub(u'\u1007', u'\u005A', output)#zg
	output = re.sub(u'\u1009', u'\u00DA', output)#nyalay
	output = re.sub(u'\u100A', u'[\u006E\u00F1]', output)#nya
	output = re.sub(u'\u100B', u'\u0023', output)#ttlg
	output = re.sub(u'\u100C', u'\u0058', output)#hwp
	output = re.sub(u'\u100D', u'\u0021', output)#dyk
	output = re.sub(u'\u100E', u'\u00A1', output)#dym
	output = re.sub(u'\u100F', u'\u0050', output)#ng
	output = re.sub(u'\u1010', u'\u0077', output)#twp
	output = re.sub(u'\u1011', u'\u0078', output)#hsh
	output = re.sub(u'\u1012', u'\u0027', output)#dd
	output = re.sub(u'\u1013', u'\u0022', output)#doc
	output = re.sub(u'\u1014', u'\u0065', output)#nngal
	output = re.sub(u'\u1015', u'\u0079', output)#ps
	output = re.sub(u'\u1016', u'\u007A', output)#fwh
	output = re.sub(u'\u1017', u'\u0041', output)#bhc
	output = re.sub(u'\u1018', u'\u0062', output)#bg
	output = re.sub(u'\u1019', u'\u0072', output)#ma
	output = re.sub(u'\u101A', u'\u002C', output)#ypalat
	output = re.sub(u'\u101B', u'[\u0026\u00C9]', output)#yk
	output = re.sub(u'\u101C', u'\u0076', output)#la
	#output = re.sub(u'\u101D', u'\0030', output)#wa
	output = re.sub(u'\u101E', u'\u006F', output)#tha
	output = output.replace(u'\u101F', u'\u005B')#ha
	output = re.sub(u'\u1020', u'\u0056', output)#lgyi
	output = re.sub(u'\u1021', u'\u0074', output)#Ar'
	output = re.sub(u'\u1023', u'\u00A3', output)#ei
	output = re.sub(u'\u1024', u'\u00FE', output)#eii
	output = re.sub(u'\u1025', u'\u004F', output)#atkara u
	output = re.sub(u'\u1027', u'\u007B', output)#a
	output = re.sub(u'\u102B', u'\u0067', output)#yc/shay
	output = re.sub(u'\u102C', u'\u006D', output)#yc/to
	output = re.sub(u'\u102D', u'\u0064', output)#lgt
	output = re.sub(u'\u102E', u'\u0044', output)#lgtsankat
	output = re.sub(u'\u102F', u'[\u004B\u006B]', output)#tcn
	output = re.sub(u'\u1030', u'[\u004C\u006C]', output)#2cn
	output = re.sub(u'\u1031', u'\u0061', output)#twh
	output = re.sub(u'\u1032', u'\u004A', output)#nhm
	output = re.sub(u'\u1036', u'\u0048', output)#ttt
	output = re.sub(u'\u1037', u'[\u0055\u0059\u0068]', output)#akm
	output = re.sub(u'\u1038', u'\u003B', output)#ws2p
	output = re.sub(u'\u103A', u'\u0066', output)#athat
	output = re.sub(u'\u103B', u'[\u00DF\u0073]', output)#yp
	output = re.sub(u'\u103C', u'[\u0042\u004D\u004E\u0060\u006A\u007E\u00EA]', output)#yy
	output = re.sub(u'\u103D', u'\u0047', output)#ws
	output = re.sub(u'\u103E', u'[\u0053\u00A7]', output)#hh
	output = re.sub(u'u103F', u'\u00F3', output)#thagyi
	output = output.replace(u'\u003F', u'\u104A')#potekalay
	output = re.sub(u'\u104B', u'\u002F', output)#potema
	output = re.sub(u'\u104D', u'\u00ED', output)#akraywe
	output = re.sub(u'\u104E', u'\u00A4', output)#lagaung
	output = output.replace(u'\u104F', u'\u005C')#akraei
	output = re.sub(u'\u104C', u'\u00FC', output)#nigh
	output = re.sub(u'\u102B\u103A', u'\u003A', output)  # ycathat
	output = re.sub(u'\u103D\u103E', u'\u0054', output)#wshathtoe
	output = re.sub(u'\u103E\u102F', u'\u0049', output)#hahtoe1chaung
	output = re.sub(u'\u103E\u1030', u'\u00AA', output)#hahtoe2chaung
	output = re.sub(u'\u103C\u103D', u'[\u003C\003E]', output)#yyws
	output = re.sub(u'\u103C\u102F', u'\u00FB', output)#yy1chaung
	output = re.sub(u'\u103B\u103E', u'\u0051', output)#yphathtoe
	output = re.sub(u'\u103B\u103D', u'\u0052', output)#ypws
	output = re.sub(u'\u103B\u103D\u103E', u'\u0057', output)#ypwsht


	return output

def logical2visual(input):
	output = input

	output = re.sub(u'([\u1000-\u1021])((?:\u103B)?)((?:\u103A)?)((?:\u103C)?)((?:\u103D)?)((?:\u108A)?)((?:\u1031)?)((?:\u102C)?)', '\\7\\2\\1\\3\\4\\5\\6\\8', output);
	return output

def precompose(input):
	output = input


	#ngr_sint
	output = re.sub(u'(\u0046)([\u1000-\u1021])', u'\\2\\1', output)
	output = re.sub(u'\u1004\u103A\u1039', u'\u0046', output)
	output = re.sub(u'(\u0046)([\u1000-\u1021])\u102D', u'\\1\u00D8', output)#with lgt
	output = re.sub(u'(\u0046)([\u1000-\u1021])\u102E', u'\\1\u00D0', output)#with lgtsk
	output = re.sub(u'(\u0046)([\u1000-\u1021])\u1036', u'\\1\u00F8', output)#with ttt
	output = re.sub(u'\u102d\u1036', u'\u00F0', output)#lgt_ttt

	#pa_sint
	output = re.sub(u'\u1039\u1000', u'\u00FA', output)#kk
	output = re.sub(u'\u1039\u1001', u'\u00A9', output)#ka_kway
	output = re.sub(u'\u1039\u1002', u'\u00BE', output)#gn
	output = re.sub(u'\u1039\u1003', u'\u00A2', output)#gg
	output = re.sub(u'\u1039\u1005', u'\u00F6', output)#slone
	output = re.sub(u'\u1039\u1006', u'\u00E4', output)#slane
	output = re.sub(u'\u1039\u1007', u'\u00C6', output)#zg
	output = re.sub(u'\u1039\u1008', u'\u00D1', output)#zmz
	output = re.sub(u'\u1039\u100B', u'\u00B3', output)#ttlg
	output = re.sub(u'\u1039\u100C', u'\u00B2', output)#hwp
	output = re.sub(u'\u100D\u1039\u100D', u'\u00D7', output)#dyk
	output = re.sub(u'\u100E\u1039\u100D', u'\u00B9', output)#dym
	output = re.sub(u'\u1039\u100F', u'\u00D6', output)#nagyi
	output = re.sub(u'\u1039\u1010', u'[\u00C5\u00E5]', output)#twp
	output = re.sub(u'\u1039\u1011', u'[\u00A6\u00AC]', output)#hsh
	output = re.sub(u'\u1039\u1012', u'\u00B4', output)#dd
	output = re.sub(u'\u1039\u1013', u'\u00A8', output)#doc
	output = re.sub(u'\u1039\u1014', u'\u00E9', output)#nn
	output = re.sub(u'\u1039\u1015', u'\u00DC', output)#ps
	output = re.sub(u'\u1039\u1016', u'\u006E', output)#fwh
	output = re.sub(u'\u1039\u1017', u'\u00C1', output)#bhc
	output = re.sub(u'\u1039\u1018', u'\u00C7', output)#bg
	output = re.sub(u'\u1039\u1019', u'\u00AE', output)#ma
	output = re.sub(u'\u1039\u101C', u'\u0019', output)#la

	return output

def convert(input):

	output = input

	output = replace(input)
	output = precompose(output)
	output = logical2visual(output)
	return output

# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.7.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x18\
[\
Controls]\x0aStyle=\
Default\
\x00\x00\x08H\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols\x0aimport QtQ\
uick.Layouts\x0a\x0aAp\
plicationWindow \
{\x0a    id: root\x0a\x0a\
    property col\
or systemTextCol\
or: systemPalett\
e.text\x0a\x0a    heig\
ht: Screen.heigh\
t / 2\x0a    minimu\
mHeight: Screen.\
height / 3\x0a    m\
inimumWidth: Scr\
een.height / 3\x0a \
   title: qsTr('\
PySide')\x0a    vis\
ible: true\x0a    w\
idth: Screen.wid\
th / 2\x0a    x: 40\
\x0a    y: 50\x0a\x0a    \
menuBar: MenuBar\
 {\x0a        Menu \
{\x0a            id\
: mainMenu\x0a\x0a    \
        title: q\
sTr('Arquivo')\x0a\x0a\
            Acti\
on {\x0a           \
     id: actionE\
xit\x0a\x0a           \
     icon.name: \
'application-exi\
t'\x0a             \
   icon.source: \
'qrc:/icons/appl\
ication-exit'\x0a  \
              sh\
ortcut: \x22Ctrl+q\x22\
\x0a               \
 text: qsTr('Sai\
r')\x0a\x0a           \
     onTriggered\
: Qt.quit()\x0a    \
        }\x0a      \
  }\x0a    }\x0a\x0a    S\
ystemPalette {\x0a \
       id: syste\
mPalette\x0a\x0a      \
  colorGroup: Sy\
stemPalette.Acti\
ve\x0a    }\x0a    Col\
umnLayout {\x0a    \
    anchors.fill\
: parent\x0a       \
 anchors.margins\
: 12\x0a        spa\
cing: 6\x0a\x0a       \
 Label {\x0a       \
     id: label\x0a\x0a\
            Layo\
ut.fillHeight: t\
rue\x0a            \
Layout.fillWidth\
: true\x0a         \
   // color: sys\
temTextColor\x0a   \
         horizon\
talAlignment: Te\
xt.AlignHCenter\x0a\
            text\
: qsTr('Este tex\
to ser\xc3\xa1 alterad\
o.')\x0a           \
 verticalAlignme\
nt: Text.AlignVC\
enter\x0a          \
  wrapMode: Text\
.WordWrap\x0a      \
  }\x0a        Text\
Field {\x0a        \
    id: textFiel\
d\x0a\x0a            L\
ayout.fillWidth:\
 true\x0a          \
  placeholderTex\
t: qsTr('Digite \
algo')\x0a        }\
\x0a        Button \
{\x0a            id\
: buttonQML\x0a\x0a   \
         Layout.\
fillWidth: true\x0a\
            text\
: qsTr('Clique a\
qui (QML)')\x0a\x0a   \
         onClick\
ed: {\x0a          \
      var value \
= textField.text\
;\x0a              \
  if (value.trim\
().length === 0)\
 {\x0a             \
       label.tex\
t = qsTr('Digite\
 algo no campo d\
e texto ;).');\x0a \
               }\
 else {\x0a        \
            labe\
l.text = value;\x0a\
                \
}\x0a            }\x0a\
        }\x0a      \
  Button {\x0a     \
       id: butto\
nPython\x0a\x0a       \
     Layout.fill\
Width: true\x0a    \
        text: qs\
Tr('Clique aqui \
(Python)')\x0a\x0a    \
        onClicke\
d: {\x0a           \
     label.text \
= mainwindow.on_\
button_python_cl\
icked(textField.\
text);\x0a         \
   }\x0a        }\x0a \
   }\x0a}\x0a\
\x00\x00\x02\xd9\
<\
\xb8d\x18\xca\xef\x9c\x95\xcd!\x1c\xbf`\xa1\xbd\xdd\xa7\
\x00\x00\x00\x05en_USB\x00\x00\x00@\x00\x05\
\x98\x02\x00\x00\x02C\x00\x11\xf9\xd9\x00\x00\x00\x87\x01\x0d\
\x1c\xee\x00\x00\x01\xa5\x03\x8bw\xee\x00\x00\x01\x1d\x05~\
\x9f\xa5\x00\x00\x02\x12\x08\x98\xc0\x8f\x00\x00\x00\x00\x0a<\
\x9c\xdf\x00\x00\x00\xd7\x0d\x89\xf5\x19\x00\x00\x00.i\x00\
\x00\x02n\x03\x00\x00\x00\x08\x00F\x00i\x00l\x00e\
\x08\x00\x00\x00\x00\x06\x00\x00\x00\x07Arquiv\
o\x07\x00\x00\x00\x0aMainWindow\
\x01\x03\x00\x00\x00&\x00C\x00l\x00i\x00c\x00k\
\x00 \x00h\x00e\x00r\x00e\x00 \x00(\x00P\
\x00y\x00t\x00h\x00o\x00n\x00)\x08\x00\x00\x00\
\x00\x06\x00\x00\x00\x14Clique aqu\
i (Python)\x07\x00\x00\x00\x0aM\
ainWindow\x01\x03\x00\x00\x00 \x00\
C\x00l\x00i\x00c\x00k\x00 \x00h\x00e\x00\
r\x00e\x00 \x00(\x00Q\x00M\x00L\x00)\x08\
\x00\x00\x00\x00\x06\x00\x00\x00\x11Clique \
aqui (QML)\x07\x00\x00\x00\x0aM\
ainWindow\x01\x03\x00\x00\x00\x1c\x00\
T\x00y\x00p\x00e\x00 \x00s\x00o\x00m\x00\
e\x00t\x00h\x00i\x00n\x00g\x08\x00\x00\x00\x00\
\x06\x00\x00\x00\x0bDigite algo\
\x07\x00\x00\x00\x0aMainWindow\x01\
\x03\x00\x00\x00H\x00T\x00y\x00p\x00e\x00 \x00\
s\x00o\x00m\x00e\x00t\x00h\x00i\x00n\x00\
g\x00 \x00i\x00n\x00 \x00t\x00h\x00e\x00\
 \x00t\x00e\x00x\x00t\x00 \x00f\x00i\x00\
e\x00l\x00d\x00 \x00;\x00)\x00.\x08\x00\x00\
\x00\x00\x06\x00\x00\x00!Digite al\
go no campo de t\
exto ;).\x07\x00\x00\x00\x0aMai\
nWindow\x01\x03\x00\x00\x004\x00T\x00\
h\x00i\x00s\x00 \x00t\x00e\x00x\x00t\x00\
 \x00w\x00i\x00l\x00l\x00 \x00b\x00e\x00\
 \x00c\x00h\x00a\x00n\x00g\x00e\x00d\x00\
.\x08\x00\x00\x00\x00\x06\x00\x00\x00\x1aEste \
texto ser\xc3\xa1 alte\
rado.\x07\x00\x00\x00\x0aMainWi\
ndow\x01\x03\x00\x00\x00\x0c\x00P\x00y\x00S\
\x00i\x00d\x00e\x08\x00\x00\x00\x00\x06\x00\x00\x00\x06\
PySide\x07\x00\x00\x00\x0aMainW\
indow\x01\x03\x00\x00\x00\x08\x00E\x00x\x00\
i\x00t\x08\x00\x00\x00\x00\x06\x00\x00\x00\x04Sai\
r\x07\x00\x00\x00\x0aMainWindow\
\x01\x88\x00\x00\x00\x02\x01\x01\
\x00\x00\x01\xc9\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 viewBox=\x22\
0 0 16 16\x22>\x0a  <d\
efs id=\x22defs3051\
\x22>\x0a    <style ty\
pe=\x22text/css\x22 id\
=\x22current-color-\
scheme\x22>\x0a      .\
ColorScheme-Text\
 {\x0a        color\
:#eff0f1;\x0a      \
}\x0a      .ColorSc\
heme-NegativeTex\
t {\x0a        colo\
r:#da4453;\x0a     \
 }\x0a      </style\
>\x0a  </defs>\x0a  <p\
ath\x0a     style=\x22\
fill:currentColo\
r;fill-opacity:1\
;stroke:none\x22 \x0a \
    class=\x22Color\
Scheme-NegativeT\
ext\x22\x0a     d=\x22m2 \
2v12h12v-12zm1 3\
h10v8h-10zm3 3v2\
h4v-2z\x22\x0a      />\
\x0a</svg>\x0a\
\x00\x00\x22M\
\x89\
PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR\x00\
\x00\x02\x00\x00\x00\x02\x00\x08\x03\x00\x00\x00\xc3\xa6$\xc8\
\x00\x00\x01\xa1PLTE\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\xfff\x00\xff\xff\xff\x03\x03\x03\xffg\x02\xff\xfc\xfa\xfe\
\xfd\xfd\x08\x08\x08\xffk\x07\x22\x22\x22\xff\xc2\x99\xfb\xfb\
\xfb\xf5\xf5\xf5111\xff\xf5\xee\xdd\xdd\xdd\xff\x93J\
\xff\xb1~\xee\xee\xee\xff\xef\xe3\xff\xb8\x89\xe9\xe9\xe9\xff\
t\x17\xffq\x11\xff\xe5\xd3)))\xffz!\xff\xfa\
\xf6\xff\xf2\xe9\xca\xca\xca\xff\xdc\xc5xxx\xff\xd7\xbb\
\x9a\x9a\x9a\x7f\x7f\x7f\xff\x9f^\xfa\xfa\xfa\xa4\xa4\xa4\xff\
\x853\x0f\x0f\x0f\x93\x93\x93\xff\xbc\x8fDDD\xff\xad\
vkkkVVV\xffw\x1c\x1c\x1c\x1c\xd4\xd4\xd4\
\xb2\xb2\xb2]]]\xff\x98S\xff\x8eC\xff\xda\xc0\xff\
\xd2\xb4\xff\xc6\xa1\xff\xa4fMMM\xff\x899\x18\x18\
\x18\x13\x13\x13\xffn\x0etttooo\xff\x8c>\
\xff\xcc\xaa\xff\xbf\x94\xce\xce\xce\xff~'\xff\xf7\xf2\xbb\
\xbb\xbb\x89\x89\x89\xff\x81-\xd9\xd9\xd9\xb5\xb5\xb5\xe3\xe3\
\xe3\xff\xe9\xd9\xff\xcf\xaf\xe6\xe6\xe6\xff\xe0\xcb\xc5\xc5\xc5\
\xf1\xf1\xf1\xaa\xaa\xaaeee888\xff\xeb\xdd\x84\
\x84\x84\xc1\xc1\xc1\x8d\x8d\x8daaa\xaf\xaf\xaf\xff\xca\
\xa7\xff\xa7m===\x9f\x9f\x9fqqqHHH\
\xff\xb5\x84SSS\xff\x9bYx\x10\xae\xbc\x00\x00\x00\
'tRNS\x00\x0f\xcc\xf1\xc3#\x15\xe9\xf8\xd5\x80\
\xacg\xf4o\x07\x1d\x0b\x92\xa1\x87A\xdcv\x989\xe2\
\xbb\xb4LH1)_\x8c\xa7XP{\x17!\x9e\xab\
\x00\x00 4IDATx\xda\xec\xdd\xcbk\x13A\
\x1c\x07\xf0\xd9W6\xbb\x9bl\x92\xdd\xec\xe6m\x1eM\
\x1c2 \x14\x95@\xc0\x83\x07\x09\x05E\x11\x04\xf5&\
J=\x08\x8a\x0aRPP\x0fV\xf0\xbf\xb6\xb5\x07Q\
k\x9b\xcd\xbe\xe6\xf1\xfd\x9cz\x9f\xe9\xceo~\x8f\x09\
\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x10W\xcb\xea-\xa6\xbe;\x0b\xbd\x81\xa9;\xb1m\x18\
\x06\xa3'\xd8\xc9\x1fv\xec\xe8\xe6\xc0\x0bg\xae?\x1d\
\xf5\xac\x16\x01iT\xc6\x0b\x7f\xb6g\xc6u\x9a@=\
6\xf7f\xfeb\x5c! \xacJTk{\xbaAS\
1t\xaf]\x8b\xb0\x0f\xc4\xa2E\xb5\xaei\xd3\x0c\xd9\
f\xb7\x16i\x04\xb8W\x19]\xf5b\x9a\x93\xd8\xbb:\
\xc2\xc7\x80[\x8d\xb1\x1f:4w\xf6\xd0\x8d\x10$\xf2\
F\x1b\xcdtF\x0b\xc3\xf4\xd9\x08\x07\x02/Z\x8b\xc0\
a\xb4pL\x0fF\xf8\x12\x94\xce\xaa\x0d\xab\xb44\xcc\
\xec\x8c\x09\x94\xa5\x15\x05}Z:;\x9c\xe34(\xc1\
\xa4c2\xca\x09fv&\x04\x0adu\x1c\xca\x19\xc7\
\xc5\x1e(\x88\xe5\x9b\x94K\xd8\x03\x05h\xf2\xba\xfag\
\x1c\xd7\x22\x90\x9b\x8a\xafS\xee\xe9>\x92\x85\xf9\x88\xc2\
*\x15B\xd5\x1b\x11\xc8X\xa5\x13S\x81\xf4\xdbM\x02\
\xd9\x89<n\xae|\xdbb\x839\x81L4]\x0e\xd2\
=\xbb\xe8\xbb\xf8\x0c\xa47\x0e\x85\xfb\xe7\xff\x8d\x0d{\
\x04\xd2\x88\x86Tp&N\x82\x9d5\xa6\xdc\xe5\xfbv\
\x11\xfb(\x1a\xee\x16\xf7\xdbT\x12\xb6\x8b\xd4@RV\
W\x90K\xffv\xea\x012\x84I4\x03\xa9\x96\xff\x14\
\x0b\xb1\x05\xb6UiK\xb7\xfc\xa7\xaa]\xdc\x0a\x15^\
\xfe\xb3-\x80X\xe02\x9akP\x89\xd5\xdb\xe8\x1eR\
x\xf9O\x19.\xb6\xc0\x7fM\xa5\xb9\xf8]\xc4\xf0\x09\
\x9c'\x92\x22\xed\xb3\x0d\xe7\x0a\x81\xbf5C\xaa\x90!\
\xee\x84\x7fj\xb9\xd2\x86\xfe\xe7\xab\x06\x08\x05\x94;\xfc\
\xffd\xd7\x08\x9c\xe9\x09\xd0\xe9\x97\x07\x1d\xb5\xe2SZ\
 p\xc1?\xa5.\xce\x012\x12\xb4\xdd'\x1b\xf6\x82\
\xa8\xad\xa2T\xec\x7f\x9e\xa1\xd2\x05\x82\xb9\x82\xc1\xdf\xdf\
\x0cu\x83Ak@\xe1\x84\xa9hR\xc0\xafS\xf8\xa5\
\xda!\xea\xb1\xb8\x9e\xf1+\x9a\xae\xdcG`.}\xd9\
\x0f\x91\xc0\x054\xe5\x83\xff\x7fy\x0a\xe5\x04zB\xcd\
\xf9\x15\xa5\x1f\x11E\xb8\xea\xa6\xfe.\x164\x88\x02&\
\x8af\xfe\x11\x0b\x9e\xa9\xe1\xf2w\x81\xfa\x94\xc8\xad\x81\
\xe8\xef\x12\xa1\xd4sdM|\xfe\x95>\x06\x22\xa4\xfe\
\xb7`K{\x1b\xe8 \xfa\xdf\x0as\x89\x8c4\x8f\xc2\
\x96\x86\x12&\x85&\xca4}g!\x96\xee\xc9\xc99\
n\x7f\x89\x18\x92\xb5\x0a\xf98\xfe\x93\x92*\x10\xe8R\
H,\x94&1\xac\x09\xff\xd2S9\x06\x92\x84\x82\xc8\
\xfe\xec\xca\x91\xa2at\xact\xdfw:\xb6\x04?H\
s\x05\xad?)\xd4\x85\x7fv\xba\x86\xf0?\x15&x\
\xabX\x9bBJm\x22\xb0\x80Bj]\x22,\x14\xff\
3\x11\x1215P\xfd\xc9\xc8\x9e\x90)!\xac\x7fv\
\x86\x02\xb6\x09\xb50\xf8\x97!S\xb8\xa4\xa0\x86\xc9/\
\xa5w\x80\x86\xf4o\xc6t\xa1^\x99\xad\xa0\xfb#s\
\x8e@;\x00\xff\xffy\xd0\x859\x05Z8\xffsa\
\x0ar\x17h\xa0\xfc\x9f\x93\x81\x10\xf9\x00\xac\x7f~\x86\
\x22\xec\x80=\x0a\xb9\xf1\x08\xf7\xd0\xfe\xf7\x0f\xa5\xea\x02\
\xa8\xff\xe5, \x5cC\xfd\xff?\x14\xe9\x0f\xa8Q\xc8\
\x1d\xc7=BW\xd0\xffU\x00\xc6\xed\xd0\xd0\x18\xe3_\
\x8508\xed\x15n\xa2\xff\xbb 6\x97\xf3\x02\x1a\x0a\
@\x85q8,\x0b4\xd0\x00R\xa0\x01\xe1\x0e\x12@\
\x05\xe20!t\x95B\xa18{`|N\xa1`\x5c\
]\x06'\x18\x00,\x5c\x9d\xa3Wdp\x01(C\xcc\
\xcfU\x00\x13\x00%\xe0\xa86\x8c\x00p{2\x06\x82\
\x11*\x00%a\x5c\xfc\x0a\xb9\x85\xf7_Kcp\xf0\
\xaep\x03-\xe0%\xd2\xcbo\x14\xc6\x08x\x898\xc8\
\x08\xaa\xdc\x02\xf2\xfc\xdb\xb3\x8f\x9b/\xc7O\x8e\x1e\xaf\
V\x1f\xd6\xebk\xcb\xeb\xeb\xf5\x87\xd5\xea\xd5\xd1\x93\xe3\
7\x9b\xaf\xcf>=\xa7\x05\x98\x92RY*\xb6\x00\xb0\
\xdb\x8f6\x07\xaf\xdf\xde]^\xe6\xc6\xe3w\x0f\x0e\x7f\
\xec3\x9a\xa3\xbaE\x12A\x00\x90\xca\x8b\x87\xdf\x8f_\
\xddX&s\xe3\xce\xc1\xcb\x87/hN\xf4\x06I\x0a\
=\xa0;\xd9\x7fz\xf0\xf8\xdarg\xab{/o\xd2\
<\xb8\xa44=e2\x0077\xef\xd6\xcb\xf4n=\
9\xcc~\x13\xb0\x88\x94DS\xa3\x07\xec\xc5\xa3\x83\xf7\
\xcb\xec\xdc\xba\xf7\xe8>\xcdT_#\x09`\x08,\x91\
\xfd\xcd\xd1\xf5e\xd6\xae\x7f>\xdc\xa7\x19\xf2H)~\
\xb2w'\x5cM\x5cQ\x1c\xc0C\x15\xa4vqi\xab\
\xc7Z\xab\xd5\xea}w\x96$d\x81\x10H\x08\x90\xb0\
\x84-\x84M\xb6\xb0\xcb*\x8b \x02\xe2\x02u\xab\x9f\
\xba\xf5P[03o\xde\xecK\xe7\xf7\x05<29\
\xf3\xde\xbd\xef\xbe\xff\xfc\x06^7\xfc\xe8\x99\x88&\x19\
\xe9\x0c\x83a~\x0f\xd8\xa0\xd2\xe33\x00\xc3\x0bY4\
\x95\xf8l`\x16\x8c`S-\xe8\xe9\x14\x08\xae\x7f?\
\x82\xe6\xebz8\xc8\x81\x11\xce\x07,w\x1d\xbck\xb8\
\xad\x16\xad\xf2d=\x0c\x06\xf8>\xc0\xc4o\x012\xe8\
\xdf\x12\xd1J\x91\xa37\xa0\x93\x0d\x8b\x80Wo\x01\x04\
\x07\xb3h\xbd\x95Q\x0et\xba\x19`\xe0\x9f\x01)\xe8\
}\xf4\x04\xedQ\xdb\xd6\x0bzX|*T\xe5\xc9\x0a\
`n=\x8a\xf6\xa9\xef\xec\x05=\xceU\x05\x94\xf8S\
\xa04\xc1\xb6=T\xc5i?\x81{\x01\xcb\xdc\x02\xcf\
\x09\xb6\xd5\xa3\xfd\x1a\xdb\x82\xa0\xdd\xfd\x00\x9d\x7f\x06 \
\x8b{\xd7\x88\xce\xf0\xf4\x80\x03\xad.\xd0\xcf\x04\xfc{\
\xa0\xb2\xfaG\xd09F\xde\x836\xf4\x00)\xff\x10X\
Vx\x0b\x9d\xe5a\x18\xb4\xe1n\x04\xac\xe0\xad)\xa0\
\xde\xbe.\xd4\xa7u;\xd7\xbe\xb3t\x5c\xf3\xc9\xd2\xd2\
N{n;\x8e\xfaD_\x04A\x93\xaf\x02\xd2\xfc\x16\
\x80\xaci\xad\x85\xbf\x90\x9c(%\xf2\x8b\xabi\x9e\x94\
\xe3S\xab\xe3\xf9\x0f\xa5\x5c\x125\xaa\xd5\xb4\x0eX\xd2\
\x0c\xa8\xf0\xd2=\x90\xd9}\xd4 \x9e+L\xcd\x84\x08\
\x8b\xd0j\xbea\xb2\x155\xd8\x9f\x03\xd5,\xd9\x07\xde\
\x05\xef\x18\xadG\x95\x84\x5ca,E\xd4\x1a\xfa\xb8\xbc\
+\xa0J\xf5\x07\xa0\x9a\x051\x92\x95\xd5\xe0\x15\xe1\x97\
j\x1f~b1D\xb4\x0a\x8d'vETek\x18\
T\xab\x96:\x14\xf2{\x80RF\xf7P\x85\xd6\xa5|\
\x9a\xe8\x95\x1e\xabI\xa2\x0a{\x83\xa0\x92\xe9\xe3a?\
\x81G\xf4v#\xbb\xc3\x86\x1e\x9e\x18\x83\x9f)$\x91\
]w\x10\xd42wF\xd8+Q \xfd\xec\x9b\xffd\
a\x86'\x14\xe6\xfe\x06j\xdf\x80*e\xa5\xa0_\x02\
J\xe0\xd6Ed#\x1c\x8f\xf3\xc4x|\xdd\x8e\x80l\
\x22m\xa0Jy\x98\xb4_\x02~i\xee1\xb2\xd9.\
\xa6\x88YR\xc5md\xb3\xd5\x0b*\x98Z\x0a^\x04\
/\x88\xd5\x22\x0bqg\x91\x98\x8a\x1f\x9fD&\x9b1\
P\xe5b\xc0$\x15\x9e\x18\x039\xe8B\x06Bi\x95\
\x98o\xb5\xd0\x82\x0c\xa2\xafA\x8dsg_\x01\xfeU\
\xd0\xd3\x82o\x91Ak\x22M\xac\x91\xfa\x10G\x06}\
\x1c\xb0;\xfb\x0a\xf0\xe7\xc0N\x9b{\x89\xca\xe2\x89y\
b\x9d\xf9b\x1c\x95=\xee\x05v\xdfU\x05\xfe\xe17\
\x81\xcf\x0ao\xa2\xa2\xb5\x864\xb1V:\xb1\x86\x8aF\
\x86\x81\x95I\x0d\xe1*\xf7\xdf\x04x\xde\x88J\x84\x86\
4\xb1^jY@%Oc\xc0\xea\xec+\xc0\xff \
\xdcg\x7fFQ\xc9d3\xb1\xc7\xea$*\x89N\x03\
\xb3\xab\x01\xc3]v\xfd)\xd0\x82\x88\x0a\x9a\xea\x88}\
\xc6\x9bPA\xe4\x00XU_\x0e\x9c\xf0\x07\x01\xff\xd5\
\x86\x0a\xe2S<\xb1S\xa8\xd8\x82t\xe2;`d\xfc\
+\xa0\xd2\xed\x83\x80\xafP\xc1\xe4\x10\xb1[s;*\
X\x07F\xd5\x95\xfe\x0b\xe0\x8c>\xa4k\xcd\x13'\x18\
k5\xea\x17p\xd5\xe0\x12\xc0\xdd;\x00\xee-\xd2\xd5\
\xa4\x893\xa4\x96\x0cj\x09}W\xe5\x9f\x02\xfc\x8b\xeb\
F\xaa\xf8G\xe2\x1ccq\xa4\xea\x006\x0f\x02\x06\xba\
\xe4\xeec\xc0\x0e\xa4j\xb7\x7f\xf5?\xad9\x87T}\
\xc0\xe4\xc2%\x7f\x0e\x80i\xff'$x\xe2,|Q\
@\x9aN`\xf2\xad?\x08tb\x1di\x92=\xc4y\
\x16[\x91\xa6\x0dX|\x1d0\xcc}p\xb1N\xa4\x99\
H\x11'\x1a\xca!\xcd;`q\xcb\x0f\x04\xfb\xdb\x00\
\xd2\x14\x9c\xf6\xfa\xff\x8co@\x0aq\x10\x18\x9c\x0f\x18\
\xe46X%\x98y\x7f\xd0\xf6\xaa{+\xbb\xf9)\x80\
?\x82\xe2\xa7\x00\xfe\xcd\xecV\xf7\xab\xb6\x81\xe9L\x10\
\xd4{\x1fAykc\xc4\xb9\xf2\x02\xca\xeb\xea\x07\x06\
7\x5c\x14\x09\x1b\x9e\xee\xec\xce6\x22]cv\xbfS\
]\xfc~,\xea\xb6\xe5\xff?3\xb4\x8d@}\x06\x94\
\xfd`\xd01\x10\x07\xa6\x0a\x8f\xf6=\xdbS\x17\xbf\xff\
:\x03L\x86\x9f\xa0\xbc&gU\x7f\xe5\x9a\xb7Q^\
\xed,(\xe2.;\xbd\x09\xc4=_8j\xd4\x1a\xbc\
\xfe\x9c\x03\x05\xc1\x15Z\xf5?O\x9c.=\x81\xf2\xb2\
AP`\xd4l\xd8\xcf`\x8e\xb9\xc1\x8e\xa7\xa8G\xf4\
\xe1\xc10Pp\x8fQ^\x8dS\xb7\x7f\xa7\x85\x96P\
^7(\xfa\xd9\xb9\x89P\x99\xce\xac\x88\xfa\x89+/\
b\x9a\x1a\x00\xcbnx\xfe\x84\xf05\xfa\x8a\xc1_\x9d\
y\x1d4\xfc\xe8\x19\x1a\xa7v=\x03R\xa6E\x94\xd5\
@\x5c\x82/\xa0\xac\xc8\x1b\xa03\xe4\xaah\x15\x07\xc6\
\xea\x1dXA\xa3\x8d\xbc\x9b\x83/\x85)\x1b\xcb\x04q\
\x8f\x04e#4\x0c\x0a\xb8*\xa7}\x19:\xd6\x11E\
3t\xed\xf7\xc3\x19\xc1\x11\x94\xf5\x07q\x93\x84\x9e\x8d\
\xe0\xf5\x80^\xd7\xc08\xc1\x81M4\xcf\xe6B/\xfc\
g\x1fe\x15\x89\xbb|\xd0q2x\xcdA\x81\x00\xb3\
\x9d\xf5h\xae\xbd\xbe0\xfcc\xc0\x1b\xef\xff\x13\x0d(\
k\x10\x14\xfc\xe4\x94-`\xe6m\x17\x9a/\xd2\x1d\x83\
O\xc2Q\x94S \xaeC\xa9\x05\xea\x87\x81\xee\x9e3\
F\xc12\xdd\x11\xb4\xc8\xe3\x18\x00\x97\x95\xaf\xff\x88\x0b\
\xf1%\x94\xf3\x92\x03\xaaj}\xdb\xc0\xef\xc1\x08\xe1\x8e\
\x08ZG|\x18[G9K\xee\xa8\xff\xbf\xc4\xb7\xa3\
\x9c\x05\xa0\xfb\xde\xf6T\xd0\xd9\x8e\x08ZK\x14Q\xc6\
n\x88\xb8\xd3|\x13\xca\xe8\x8a\x01\x85\xceC\xe1J\xd0\
-\xf8h\x0f\x1d\xe3\xd0\x99\xe3\x1f,\x86\x92(c$\
\x08T\x95\xb66\x01\xa6k\xd19\xe2\xab\xc4\xbdz\xd6\
P\xc6\x0b\xa0\xban\xe3\x0a\x90y\x89*\x09\x87\xed\xa5\
Bbjl|\xbc\xa7g\xa3y\xa3\xa7g||l\
*Q(\xb5o\x0b\xa8\x97\xb0H\xdc\xacNDi\x91\
\x18\xd0|e\xdb\x0a\xc0\xb5E\x91]|\xa20\xb58\
\xc4\x139\xfc\xd0b\xbe\xd0\xde\x8a\xdaM\x11wK\xa0\
\x8c,\x074\x956M\x02\xc4\xb2\xc8\xa8e\xa2\xa1n\
\x88\xb0I\xd5}\x98hA-J\xc4\xe5\xf8\x1dm\xe7\
\x82\xd7m\x99\x06\x0f\xbe\x8a \x0ba\xa2\xa8:\x88\x91\
\xef)\xb6\x0b\xa8R\x93[\x0b\x00\x86R \x1a\x06\x0a\
\xcdk\xc0\x1d\xd0.\xb3\x82\x0c\x925c\xf3D\x9bP\
\xddr\x12U\x887\x13\xf7\xdbhAi[@s\xc7\
\xfa\x15\xe0 \xca\xf0HJu\xbc\xce\x8d\xb1\x8a\xcc\xd5\
:\xe2\x05y\x94\xf1\x1e(\x1eX\xbd\x02\xccn\xa1\x92\
\x96\x92!\x19\xac\xfcbM\x0b\x9e\xe2\xad\x0e\xb0\x84c\
\x94\xb6\xc9\x81\xbc\xaf\x0d[\x01\x8c\x8a\xe2l*\xa6\x8d\
[\x18\xa7v\xff\x17\x1b\x80\x13\xe9$J{\x04\x14w\
\x8c\xf9@\xbcAQ\x9c\xc2\xd2\x0c1V\xcf\xb1\xa0\xf0\
O:\xfb\x06\x80\x1a\x8b2\xff\xd5\xfa9\x90w\xdd\xc2\
\x0ba\xc1\x0e\xa4Z\xabY%\xc6K%\xe2\x88\xde\x19\
\x01\xa1i\xd00\x1br3\xa0A\x05\x07\x1a\x0c\xaf \
M\xdc\xb4\x0c\xd6y\xcaO \xe7\xce#@i\xa1&\
\x94\x14\xc9\x80\xac\xea+V]\x09\x8e=A\x8a\x96B\
\x8a\x98'$\x97\xb9*l\x10/\x99\x11P\xd2>\xc8\
\xbbeQ,T\xff\x1e\xca\x13\x0a)b\xaetC\x8b\
7f\xc0\xe8\x96Q\x92\x18\x03YW\xad\xb9\x10\xf4\x9a\
\xb6\xfdk_%\xe6\x1b*y\xb8\x02\xf8,t\x88\x92\
\x8e@\xd65K\x8a\xc0N'\x84p\xce\xe4\xf0,q\
\x86xM\x1dJ{N)\x04-(\x02_Q\x16\xff\
D\x88X\x85\x9fZ\xc3\xd3j\x88\xf7\xec\xa8n\x08\xab\
\x1f\x0c\xbb\x09*\xf5\xa1\xac\x89Ub\xa5\xa1\xd3\x7f\x9f\
5\xf7\x0e\x01\xc9k\x16\xd4\xbe\x02~\x09\xa8t\xa5\x1a\
\x8c\x8ab\x5c\xb3>\x837\x1f\xf7d\x0b@\xb1\x19p\
d\x5c!x\x1f\x8c\x8ab\xcc5\x13\xeb\xa5&\xf1\xc4\
\xa1\xd7v\x80'\xe6\x93(E\xcc\x80\x9c_\xcd\xfd:\
@\x87\xfc\x07\x18xb\x07\xfe\x0f\xc1C\x87\x80\xe5\xf2\
j\xdb\x81w\xd5\x9e\x04\x1a\xb3\xff;\xb4o\x0b\xde\xb3\
\x8d\x88\x13\xc4\xa3\xf8&\x94\x12\x9d\x03\x19_\x99\xd9\x07\
~\xe1\xc8\x14\xbe\xf9\x1dDw\x8f\x81\xd2\x8c\xa9L\x11\
\xe5*\xcc\xdb\x02,\xa0\x8c\x06\x9e\xd8\x89/N\x12\xcf\
\xe2wQJc\xd0\x98M\xc0]`7(:6\x85\
\xcf\xf99P\x86w\x83FA\xc6\x8ff]\x08x\x1e\
ue\x0a\x9f\xfb\xe5P\xcaK\x90q^U\x17\x80\x03\
V\xe1F\x97\xa6\xf0\xb9^\x1dJ\xca\x80\xb4\xeaK\x01\
v7\x80\xd5\xdc\xa6kS\xf8\x5c\xafI\xddGen\
\x98q\x10\xc0m\xa1\xa4Io\xf6_\x9c%O\xd9\x06\
\xea<\x0e\xf8Fg\x01x\xec\xa5\x11\x1c\xc7\xe2\x93\xaa\
Rc\xee\x990\x0b0-\xba7\x85\xd3\x03\x8a(\xe5\
\xb1\xfe\x99\x80*`\x13\xdess\x0a\xa7\xfb\xcd\xaf\xa1\
\x84\xc8,H\xab2,\x1d\x96\x1e\xc5W\xf2\x9f\xbfU\
\x96Q\xca\x80\xeeV\xd0E`\xd2\xe7\xa5\x14\x1eW\xda\
P\xb5\x06<0x\x0f\xd8/\xa2\x84\x1d\xff\xf9[h\
\x17%\x88\xb3 \xe9\x1bc\xf7\x80sO=\x95\xc2\xe4\
NS(e@\xe7.\xb0\x02X<\xf4X\x0a\x93+\
\xcd\xb7\xa8i\x07W\x18\x19\x0f;\xea\xb9\x14&W*\
\xa9Y\x03n\x18\xf8\x9d\xd0\xb9F\xef\xa50\xb9Q\x9d\
\x9a#\xc1o\x0d\xbc\x13\xd4\xed\xfe\x18vO\xe0[U\
|M\xe6\xaaq\xd7\x82\xdf{2\x85\xc9\x8djPB\
#\xa7\xeb\x92\xf0\x05P\x12\xac\xf5r\x08\x83\xab\x8c\xab\
\xb8 p\xc1\xb0F\xf0\xbaWS\x98\xdc\x87oU1\
\x1aX\xa1\xbf\x08\x90O\xe3\xffH|\x16\xa2\xaf\x01Y\
J\x19`@\x11p\x84\xe5\x96\x88\xcf\x16c(!\xd2\
\x0bR~\x0b\xb0\xf8\x11\x14\xbc\xc1r\xc94\xf1\xd9b\
^@\x09\xfd \xe5\xa2!'\x01\xdc\x0a\x96\x11\xfd\x0e\
\x80m&\xd87\x01\xf7\x0c\x99\x08\x1e\xf5p\x0c\x9f\x1b\
\x15\xe9'\x82\xea\xaf\x07\x9d\x03*n\xd3_\x00\x1ce\
\x03%D9\x90p\xce\x88*\xf0\xb5gsX]J\
\xba\x10\x8ci\xae\x03o\x03\x15W\x8be\x8e\x89\xcfF\
;\xecG\xc2\xb7\xf5_\x0b\x1c\xc02-\xfe\x1d\x10[\
\x15\xd9\x8f\x03n\xe9\xfeR\x1cW\xeb\xfd\x186\xb7\x99\
A\x09+\x9a\xcf\x03\xef\x02\xcd\xa0\xc4\x0e\xd0?\x03\xb0\
\x17\xdf\x82\xe5\xba8\xad7D\xef\x01M\xd6\xef\x01;\
\xcf\x04\xf3\x1d\xc1\x1fX\x0e\x83U6\x01w\xfd)P\
\xbb50_\x10:\xaf\xf7{\xf1G~\x09\xe8@y\
\x94\xf0B\xeb\x5c\xe8w /,\xfa/\x00\x07\xda@\
\x09\x0f5v\x82\xae\xa8\xbc\x0b:N|v\x0b\x09X\
n\x13\xa4\x5c\xd2\xf5\xb1H\xee)~)G|\xf6k\
b.\x03.\xeb\xca\x86\x98\xf6w\x00\xcet\x8c\x12\x86\
\xb5\xb5\x02o\x81\xbc-\xfc\xd2\xb6\xbf\x03p\x82\xbf\xd8\
\xbb\x0f\xa5(\x82 \x00\xa0\xcd\x89x\x80b@1\xe7\
\xd0\xdb{\x019T\x10\x10\x14\x0ce\x0e\x98s\x0e\x94\
\xa8\x98s\xce_mYV\x19v{n\xe7\xf6\xc6\xbb\
\x1e\xaa\xdf'P\xcb\xf5LO\x87^b|L\xd7 \
\xba\x12\x8d\x8e\x97&\xdd:\xdeIb\x8fus\xc0\x9a\
j2\xc1\xd7(jD\x93\x80\x22\xdc \xc6\xeet\xb9\
\xe0\x96J\xb2\x80\xfd\x81\x92\xe0\x181>\xa5k\x11\x9f\
SI\x12@[\x01e\xc8\xe5)n<\xdd\xcc\xe8v\
4\xd9I\xff\x98\xcc\xa3\x98\xbd\xf3\xc0\xf6=pA\x15\
%\xa1c\xfa\x0c$\xd6.\x8a\xbb\x8f\x8c\xd6\xf4\xabb\
\xd6S\xd4F=\x02J\xc1%\x02\xba\xd3\xad\x8ei,\
[\x0a4\xe9\xd71y\xea\x161\x8a\xa9\x9e\x033h\
0\xa1\xcf\x00r\xf5\xda\xa6\x023\xa9W\x85\x14\xbb)\
bD\xb3\x80b|\xb0-\x0cnN= \xea\xb0F\
\x00\xc1\xbe\xdb\xb6\x87u\xa4\x1e\x0e\xf0F#\x80`=\
\xc4\xb8\x88q\xd3R\xf7\x05\x9d\xa0\x88a\xbd\x03\xc8q\
\x83\x18\xdf\x5c~\x00\x07J\x141\x89\xf7\xf1\xf8\xe7\x92\
mU\xe0\x94\xb4\x15a_\xf4!P\xb2\xfd\xc4x\x8b\
q3 I\xd6v3\xb8N\x84\x11\xe4.1\x9ec\
\x5c\x16\x92\x84\xc8\x1a\xa7\x88\x07\x81\x92c\x9bm{`\
\x08I\x90\x15>\xd5K\xa0d\xc7\x88q\xcd\xe1\x07\xb0\
U\x8f\x00\xa29\xfc\x00B\xe4\x1c\xd5R\x00\xd1\x1c\x86\
\x80\xac]C\xc0F\xcd\x03K\xe2\xf0\x108\xc3n6\
\xfc\xae@\x09\xe2\xf0\x1a8\x059\x9b\xb4\x1aP4w\
\x89 \xfe\x038P\xa0\x88=\x81\x12\xc4a*x\x1a\
26P\xd4\xdd@\x09\xe2\xf01h\x112\xbeQD\
^_\x82D\xd9\xe3\xee9\xb8\xd9\xaa%d(P\x92\
8,\x08\xc9 \xe3\xa0>\x05\xca\xf6\xd5]IX#\
2N\xeahX\xd9\x1c\x16\x85.\xb6\xaa\x069\x12(\
In\xba+\x0boE\xc6\x00E\x9c\x0e\x94$\x0e\x1b\
C\xda\x91Q\xa2\x88\xfd\x81\x92\xc4ak\xd8*\x8c;\
\xa0\xd5 \xb2\xb9l\x0em\xb1\xea\x0a\xd34\x80(.\
\xdb\xc3\xdb0\xee\x05E\x0c\x07J\x12\x97\x03\x22V\xda\
T\x84\xf6\x05J\x12\x97#b\x96b\xdcQM\x04\xca\
\xe6rH\xd4B\x8c;\xa5\xd3\x01e\xbb\xe9pL\xdc\
T\x8c{\xab\xa3Ads9(r6\xc6\x8dj=\
\x90h\x0eG\xc5\xf2\x15!\xd7\xf5-H\xb4\xfd.\x87\
EC\x87\xc5k\xf0\xc3@\x09b?.\xbe\x19\x925\
\xea\x07\xe0\x1b\xb7\x0b#Vk\x08\xf0\xcd\x0e\xa7+c\
V\xe9!\xd03\x9dn\x97F\xb5\xe95\xd03\x8e\xd7\
\xc6\xad\xd5D\x90g\x8e\x10\xe3S\xea\xc5\x91\xcb5\x15\
\xec\x19\xc7\xabc\x9b\xf41\xc8/\xae\x97G\xc3\x94\xe4\
\xe7\xe0|\xa0\xc4p\xbd>\x1e2Z\x10\xe2\x95#\xc4\
\x18GN\x06l\xb4jI\x98W\xceZW\x83`;\
\xd8\x98\x8b1{\xb5(T\xac\xaby\xbe-\x8c\xd3\x02\
6\xa6kY\xb8ON\x13\xa3TD\xceJ\xb01O\
\x1bC|\xd2E\x8c'\xc8Z\x086\x9a\xb45\xcc#\
\xfc%p7\xb2\x1a\xc0\xca4m\x0e\xf5G\x0f\xd9g\
\x01\xa6\x81\x9dF\x8c\xfa\xac\xa9@\xa9\xba\x881\x10\x22\
g1\xd8Y\xa0\x03\x22\xbc\x91\xdbH\x8c}\xc8\x9a\x03\
v\xa6\xeb\x88\x18o\xf4\x10\xe7\x14\xb2\xa6\x83\x9dy:\
$\xca\x1b\xe7\x89Q\xb8l{\x09\xe05\xe8\x988_\
\x5c\x1d&\xc6k\xe45\x80\xa5\x0e\x1d\x14\xe9\x89\x0f\xc4\
\x19EV\x07\xd8j\xd5Q\xb1\x9exL\x8c\xd2ed\
\xad\x06[\xeb0\xea\xa8\x9e\x02%\xdaO\x9cq\xe4\xcd\
\x07[Ku\x5c\xbc\x1f\xba\x88\xf3\x1cy\xcb\xc0V\x93\
\xc5\xc2\x88\xf3\x81\xaa\xb7\xc1\xdb\xc4(]A^\x13X\
[\x94\xbc2\xe6e\xa0\xea\xad\x978\x13\xc8\xeb\x00{\
\xabui\x94\x07r}\xc4\xf9\x86\xbcv\xb0\xd7f\xb1\
9\xf6C\xa0\xeak\x0fq\x06\x8a\xc8k\x03{\x0b1\
\xaa\xa8\x8b#\xc5\x19\x22\xce\x1d4X\x08\xf6ff1\
jLW\xc7\x0a\xd3C\xac\xad\xc8\xcb\xce\x84\x0ad,\
\x96G\xf7\x04\xaa\x9ev\x10\xe75\x1a4B%V\xe9\
\xfax\xe9z\xc8\xfc\x10h\xec\x0b\xad\x22\x15T\xec\xa6\
\x88\x8d\x1a\x03\xea(7d<\x02\x9a\xd3@\xf6\x1aB\
\x8c:\xa91@\x92\xd3\xc4\xda\x89\x06a\x03@u\x87\
\x80Q\x8d\x01\x82\x18~\x00\xba\xaf\xa0A\x06*3\x87\
\xe9\x0f\xd3\x18 \xc7\x05b\x1dD\x93UP\x99\xb5\x18\
3FZ\x16$\xc5\xd5\x11\xe2\x94\xd6c\x8a#\x00k\
v\x16\xa3v\x92\x0e\x0a\x91\xa2\x9fX\xcf\xd0$;\x1b\
*\xb48\x1e\x03\x0a\xbaAZ\x88myb\xbd@\x93\
%P\xa9\xf9\x18\xb3\x9d\xb42P\x86s\xc4\x9a@\xa3\
6\xa8\xd4\x0a\x8c\xb9\xa6\xc7@\x19z\x88U\xd8\x80F\
S\xc1\xc8\xbe&\xe0xI\x9f\x04%\xb8\xdaG\xacw\
h\xd4\x01\x95[\x801\x13\x14\xf5RkCk\xefV\
\xe2\x0f\x00\xdf\x13T\xfdE\xf0\x22\x91\x0e\x0a\xa8\xbbK\
\x05b\xedC\xb3\xa5P\xb9\x86,F\x85\x8fH'\x06\
\xd6[\xe7\x10\xb1J[\xd1\xd5%\xd0<5\xfa\x15\xe9\
\x83@\xbd\xf5\x13\xef \x9a-\x864\xe6\xa3M*\xe0\
\xb1\x9e\x02j\xeaF\x9eX\x9b\xaf\xa0\xb3K\xa0\xf9\x22\
\x88\xef\xf4'\xa0\xbe\x06\xfb\x887\x8ae\xac\x80T\x9a\
1\xe6#\xc5\x0c\xe9O@\x0d\xdd$\xde\x89\x10\xcd2\
\x90N\x0b\xc6=!}\x12\xaa\xa3\x0bd\xf0\x05\xcbX\
\x07\xe0,\x06|\xa3\x98>M\x07\xd6\xca\xdda\xe2\x9d\
\xc4r\xa6\x028\x8b\x01\xe1&\x8a\xe9\x0dTM\x0c\xbe\
$^\xf7z\xac2\x02\xf0\xd6a\xdcs\x8a\x19\xd6&\
\xa1\x9a\xc8\x9d\xa34'@\x9c\x0fiME\xbb\x9f\x80\
\x9b\x81\xaa\x81\xafd\xb0=\xac>\x02\xf02\xec\x1eY\
M\x08\xd7EO\x81x\xa5\x0d\xe8<\x02\x98sA\x18\
\xde\xa3\x98\xbe\xc1@\xfdg\xfb\x87\xc9`7\x96\xd5\x06\
\xe9ME\xc3.q\x1d\x1d[k\xc7\xfa\xc8\xe0D\x11\
\x93\x22\x80\xdb\x18\x10\x8eQL\xe1F\xa0\xfe\xa7\xabC\
d\xb0w\x03\x96\xd5\x08\xd5hC\xc6\x8b\x82\x06\x81\x1a\
\xcb\xed\x22\x93\xcf\xe8&\x02\xf0\x9a\xb2\xc8xF\xfe\xde\
\x04\xf6\xf8\x98\xb9\xce\xbd'\x93q,/\xdb\x04UY\
\x8d\x8c\xe3\xdd\xe4kF\xf84\x1d\x0a\xbc\x93\xeb\x22\x93\
\x81\xcbX^;Tg\x1er^Q\xdcm\x1f\xd2A\
\xc76\xfa\x98\xb8\xec'\xa3\xa3\x98`\x1eT\xa9\x03\x19\
\xc5M\x147$\xffM\xa0\xf3\xb1\x8f\xebN\xbe\x92\xd1\
AL\xd0\x01\xd5Z\x87\x9c/\xc4x\x1fH\xd7\xe5c\
-s/\x19=)b\x82\xf9P\xad\xa6\x109\xfb\x88\
\xc8\xbb\x22\xf1\x0b\x1e6\xb4\xe4\xfa\xc9h\xe08&\x08\
\x9b\xa0j\xad\xc8\xb92@q\xf93\x81d\x97\x86\xfd\
ki\xca\x1d\x22\xa3\xbd\x1f1I+To)\xb2N\
\x11\xe3\xb6\xe4\x09\xc2\xdbF\xe8\x8f[~\xdc\x06s]\
d6\x8a\x89\x96\x81\x03\x8b\x90\xf5\x8e\x18/\xb7\x04R\
\x0d>\xa0\xbfu\xf9\xf0\x05t>$\xb3}\x98h\x11\
\xb8\xd0\x82\xac\x03\xf7\x89\xf1X\xeaU\xa03\x9aK\xdb\
%?w9\xb8\x83\xcc^\x171Q\x0b\xb80+D\
\xd6\xe1\x021\xce\xc9\xfc\xcf\xca\xdd\xa4\xa8!\xe9\x89\x8b\
m\x0f\xc8l\xd3\x15L\x14\xce\x02'V#\xef\x0dq\
\x1eJ\xfc\x02\xd8X:\x22{\x03\xf2\xa5\x112\xdb\xbc\
\x1e\x93\xb5\x83\x1b\xcb\x91W\x1c#\xcey\x81_\xc0!\
\xe2\x0cK.d\xb9\x90'\xb3\xee\x17ha98\xd2\
\x88\xbc\xf5\x9b\xe97\xd1'\xec~\xfa\xc3\x8f\xa3`g\
\x17\x95Q8\x8a\x16\x16\x83+K\xd1\xe0b\xc1\x87?\
k\xb9\x5c\xcaY\x99\xd7\x96c;\xa8\x8c\xc2(\xdaX\
\x06\xce4\xa3\xc1nb\xbd\x97\xf4\x05\xe4nQ\x19}\
\x97\x02y\xce\x8cP9\xd7\xd0F3\xb83\x1d\x0d\xc2\
\x09b\x9d\x93s\x1b\xcc\x9d\xa7\xb2\xf2\xbd\x92\xbe\xd6\x9f\
r\xbdy*g7ZY\x09\xee\xcc\x9c\x86\x06\x07\xee\
\xd1/Ro\xd9\x9d\xe7(\xc9\x0eY\xf7\xc1\x1f\xec\xda\
wW\x1aA\x10\x00\xf0EcI11\xa6\xf7\x9eq\
\x8e\x83 U\x14\x13TDT\x04;(\x16\xc4\x88\xbd\
Dc\xef\xd1\x18\x93O\x9d\xe4\xbd\xbc\x94\x17\xefn\xef\
\xb8\xdb\xdb?\xee\xf7\x09\xe61\xc3\xec\xcc@c\x0b\xca\
J\x02\x95\xb2kDG\x97@\x8a+\x84?\xf1\xbae\
7\xac\xa32\x1fO\x7ffi\x9f\xd7%\xffp\x87\xe8\
\xc9V\x01R\xbc\x1eD\xe4u\xcb^\xaaC*\xa3\xbc\
4\xac\x86\x8f(/)\x00\x95\x8aR\xa2\xab*\x90\xf4\
\xd5\x81\xbcn\xd9\x81y\xa4\xd4\xccE\x13\xb0\xb7\xfbP\
\xde\x22P\xaa\x22\xfa*)\x07I\x93\x9cn\xd9\xf6\x1e\
\x07\xd2\x1b\xe9\xaf6[c+*h\x03J\xe5\x95D\
gwA\xda\x1e\x97[\xf6\xfb\x8f\xa8\xca\xfc\xb1\xb9\xf5\
\xfa\xa6\xb6\x09\xe59\xf2\xc0\xa0\x01H\xa8,\x07i\x8b\
(\xa1n\xaa\xda,\x9d\xbb\xa8\xd6j\xa0\xda<\x01\xc5\
x\xdd\x87\xc0\xa0\x01H\xaa\x02\x191\xc9\xa2\xed2\xe7\
\x22`?\x16Q\x83\xd6\xa5js\xcc\x8d\xa0\x12O\x16\
\xa8='\xfa+\xad\x00iB\x1c\xa5\xac\xcfU\xb3\xd7\
?\x8c\xda\x88]f\xec\x03\xfd5\x22*Y\xf3\x02\xb5\
\x8aRb\x80\xe7 C\x88\xa1\x94\xf91\x06o\xab\xd2\
0M\xaf\xa9\x9eu\x09\xbc\xadoBE\xa9\x01\xa0w\
\x93\x18\xa1\xb4\x18\xe4$QR\x8br\x13`5L\x87\
P\xd9<\xd3\x12x[;\x8f\xca\x16\x12\xc0\xa0\x01(\
\xb8\x09\xb2\xf6\xf8\xb8\xb7\xdb{\x9aPR\xcc\x19C\x0a\
\xbeZV\xebK\x7f=M\xfa\x1d\x07\x02\xa8p\x89\x18\
\xc3V\x0c\xb2\xdaP\xda*\xab\xabP\xe6\x9d\xc2\x19e\
\xd0\x83\x14\xc4Q\x16]k\xa9\xa6\x09)x\xfa@\x8d\
b\x1b1\xc8%\x90w\xd8a\xf6\x80\xdd8\x8d\xd2\xdc\
y\xf8\xc9\xebG\x1a\x8e\x8f\x06\xaf\xb0\xf6@+RY\
\x0e\x83*\xaf\x89Qle \xaf{\x13\xa5\x893F\
\xf7\xd5\x86z\x91f\x8d\x9aX@:\xab=\xc6E\xdc\
\xd0\xb3\x8bt\xd2\x09P\xa5\xccF\x0cs\x05\x14\x84\xfd\
(C\xac1\xb2\x04\xde\xf7\xf8(\xd7(a\xcf\x8dt\
\xc4\xe9\x80\x11\xd3\x8b=0\x22\x22\x9d\x8eIP\xe9\x19\
1P\x11(\xc8EP\xce\xfc\x99Q\x03\xf6\xdbZ\x1f\
\xcaI\xb9\xe0/;~\xa4\xd5\x5c3n\xd77\xfb\xe3\
]\xcdHk\xd9\x0b*\x15\x11#\xdd\x03%\xce\x98\x19\
\xd3Uc\xbd\x0fe\xc5\x9d\xf0\x8fD\x1c\xe9\xd5u\xe9\
V\x03\xf6\xa9\x19\x89\xec\xcb\x87M\xef\x161\xd4eP\
4\xe8a=]u~\x12Q\x96;\x0a\xff\xe9\x0b\xa2\
\x0a\xcd\xd3c\x0d\x85\xbf\xfbC5\xcd\xa8B(\x0b\xaa\
\xbd \xc6*)\x07E^?\xcb\xe9\xea\xfd\xd8:*\
\x08u\xc39\x5c\x0b\xa8\x8a\xd8R\x9by\xa3=\xcc\xc0\
\xd9:\xaa\x93\xce\x81j\xe5%\xc4`7A\xd9D\x1a\
\x95\x88\x9ft\x99\xae\xec\x99\xd1&T\xb2\x90\x93\xeaU\
ATI\x5c\xef\x1a\xeaW\xff@}\x9by'\xa2J\
\xa1A\xf8\x85\x87\x1b\xd0\x1f\xd7\xcb@\x09\xe5\xb5\xc57\
\x1a\xb03\x98\xa6:\xda\x04\x90\x92\x8b\xa3\x06\xbe\x96\x9a\
\xe3q\xba^\xf0f\xae\xbd~\xa4\x195\xd8\x9a\x00\x0d\
\xee_'\x86{\x064\xc2\xb3t\x13\xf6\xd0[\xad-\
u\xa8\xa6\x0e)\xa4\xbc '\xbb\x82\x1a\xd5\xb5\x8c\x9e\
\xb5g\xe6\x1a\xec\xe7\x95f\xc3\x5cf\xec\xecSK\x1d\
j\xe4\xef\x06M^\x12\x06\x8a\x80\x86s\xd1M\xfb\xb2\
N\xa9}Y\xdf\x8c\xd7\x0e\x8bH\xc3\x91t\x82\xbc\xc4\
A\x07\x16\xc6\xb7\xda\xd2:2=]\xf3\xd3\xf4\xf4H\
k\xcb\xaa\x0f\x0b\xe3is\x82&\x17\x08\x0b\xf7\x04\xa0\
\xe2\x8d\xd0\x8fW\xf5\x01\xda\x97\xb5?p6\xdc\x84\x94\
\x96O@\x99k\x0b\xf9\x92v\x816\xc2=\xc2D\x15\
m<y\x0f\xd2\xf3\x0d\xcf\x8ce\x1a\xed\xd2/~\xe3\
\xd4X\xd7\xb0\x0f\xe9u,:\x81Jw\x0a\xf91{\
\x02ZU\x116l\xf7\x81\x92k\x01U\x12w\x87G\
\xbbj\x8f\xbfe2\x9d\x9dK\x8dK\x9d\x9d\x99\xcc\xd0\
Xm\xd7h\xeb\xae\x88*\xed\x87\x81\x96\xd0\x1bB>\
\xac\x1c\x0a Ov\x02d\xe41\xfc\x8b\xc7/\xd7\xca\
 \xa8\xe1\xcc\xf3P\x02\xa1\xa8\x13\xb4{D\x98y\x01\
\xd4\x84\xfc&j\xc0~\x8crF\x83\xa8\x0e_\xe9\x87\
\x1b\x84\x9d\xd22\xa0\x97Kv [\xee\xcf\x03\xa0A\
bo\x13\xcd\x13,,\xfdPVJ\x18z\x06j\x0c\
\xc4\xdc\xc8\x8ec+\x0c\x1a9\xf3~4\x87?\xef\x84\
\xc2\xbc$L=\x00U\x5c\xccJ\xc0\x91\xf6B\x01\x84\
l\x04\xd9\x9b\x1d\x14\xa0@\x0f\x09[%\x15\xa0N8\
\xc6\xe2!\xe8\x88{\xa1P\xdd\x1f\x1c\xc8\x92\xfb\xe8\x04\
\x0aVQB\x18\xbb\x03j\xe5\xda\x82h\xac\xcd\xe4\x00\
\xe8!\x17\xf5#++\x8b\xba\xc4|\x950w\x01T\
s\xf6\xa6\xd08\xcb\xa7\x09\xd0\x8b\xd0\xbd\xc5\xa4am\
u\x83..\x10\xf6J\x8aA\x03o\xcc\x83?\xf0\xfb\
Q\xfe\x96\xcbG\x1ch$\xc7~\xef\x04\xe8\xa3\xb8\x84\
\x98\xe0\x19h\x92\xe8\x8d\xa0\xdef\xf3\x090\xc0@~\
\xc3\xb0\x1a\x88\xe4s\xa0\x9b\x97\xc4\x14/@\x15\xa3>\
\xd8T[\x18\x0c\xe3\x8a\xee\xbbQo\x1d\x0b\xa7\x03\xa0\
\xa3\x1b\xc4\x1c\xb6\xfb\xa0\x99+\xaaK\x83uDh\xb3\
\xaf\x9d3\x1b[A\xfd\xac\xc5\xfb\x12\xa0\xab\xdb6b\
\x92{\x02\x14`\xa2/\xb6\x86\x85\x08nm\x0f\x00\x1b\
\xde\xc9tH\x8f\xe4\x1f\xe5\xf5\xafW\xe1\x161\xcd\xcd\
Bc\xf7\xe6\xb7\xb4\x15A\xe8\xe8tG\x00\xa6\x5c\x83\
\xb1\x94\x035\xf3\xc7\xb7\xc3`\x84K\xc4DEP8\
\xd7`r\x7f\x13\xe9mn\xc4\x0e]`\x8e\x89\xee|\
,\xe2Au<\x91X\xefI\x02\x0cRt\x8d\xa8\xc3\
\xc1.x\x0eW6\x1a\xdfXS\xea\xa0\x1b\xf1h\xd6\
\x05f\x13\x5c_'\x93\x1fR\x1e\xe5\xcc\xa7\xd2\xc9S\
C\x03\xd6x\x024\x7f\x17\x94\xe0\x0c\x7f\xd9\x8e\x1e|\
No,\xfbW\x82A7\xba\x83\xc1\x15\xff\xf2F\xfa\
\xf3At\xfbK\xd8\x09|\xc9\xedd\x0f'\x17cG\
\x1b\x11\xff_\xe1\xfa#\xfbG\xb1\xc5\xc9\xc3\xecN\x0e\
\x18xILv\x17,&\xbaK\xccv\xad\x08,\xa6\
)\xbaFLWY\x06\x16\x93\x94U\x12\x0e\xdc\x12\xc0\
b\x0a\xe1\x16\xe1\xc2\x1d\xb0\x98\xe2*\xe1\xc4e\xb0\x98\
\xe02\xe1\xc5\xf5\x8b`a\xee\xa2\x8dp\xa3\xa4\x18,\
\x8c\x15?%\x1cy\x05\x16\xb6\x84W\x84+\xd6 \xc8\
\xd8\x1d\xc2\x99*\xb00\xc3\xc3\x05\xf0?\x0f\xc1\xc2\xcc\
C\xc2\x1f\x9bu\x13f\x84\xaf\x05\xe0\x8f\xca\xfb`a\
\x80\x97\x0b\xf0\xff\x9eZ\xcb \x13\xc5O\x08\xa7\x1e[\
\xbf\x0a\x18\x8e\x9f_\x00\xces\x05,\xdf\xd9\xbb\x17\xe5\
\x04a \x0a\xa0Q\x9e\xa2\x88 Z\xa8\x8eS\xab\x9d\
\xcc\xf0\xff\x1f\xd8\x99\xbeE\x91WR7\xd9{~!\
1d77Q\xbb\x85 ,\x97\xa0Y$H{\x95\
\xa0U&\x88CDL\xab\xb5 \xef$A\x13J'\
\xc0\xcd\x12\xb4\x04\xb5\x99\x13\x88\x00b\x06<\xce\xce\x88\
\xf1\x17\x22u%h\xe0\xa6\xc2\x108\x16\xd0aJ\xf2\
\x00\xe06\x1f\x191\xe5f\xbe0\x08\xd6\x00\xd5\xa6F\
\x8d\xbf\x10\xe9N\x82B\xaeA\xeb?f\xc0\x07\xa6\xfb\
\xbf_\x09n\x0b(\xb37\xa4\xfe\xabYKP\xe2d\
\xe6\xf8c\x06(A2\x00\x8a\xa8p\x1bN\xe7\x7f\xc8\
\x07\xdc\xc0\xe6\xfc\xbf\xcd\x02)\xb1Q*\xd2\xf9\x9f.\
6H\x8a\x8e\x10\x1f\x84\xf1^\x90\x16\x1f, \x9b\xff\
\xedc\x85\xb6\xf0@3\xa2\xf9\xff\xbeR\x04\x04\x06\xd9\
\x19\xd7\xfeE9\xa8\x8e\xd1\xe5\xff\xb5%\x8a\x81~\x8c\
/\xff\xea\xdeP\x0c\xf4\xe2\x10{\xffa<\x0f\x19\x91\
\x1ef\xa4\xde\x7fQ#\xc5\xe9`gs{\xb6\x7f\xd8\
\x08\xf4W\x91{\xfeE\x95\x0d^\x95\xed  |\xfb\
w\xac\x15\x02\xe3\xad\xa6\x9e\xb0X\x82\x8e@\x8b\xc2\xd4\
\xf0GW\xc7XB#\xe7\xe1\xff\xff\xa0\x9f\x87\xcf\x00\
\xd3\xe5\xffG\x84j\xe0\xa6*\xb7}\xf9\xffVn%\
\x5cy.\x05\x1b\x13\xc4Ek\xacm\xfe49\xe3l\
\xe0\x0f\x1e\xbb?\xec\x05\x9b\xb9<v\x7f\x97\x16(\x08\
\xbf\xc4\xd6\xf6~\xef\xf3p}\x90\xef\xcf\xff\xd3\x19\x87\
\x03\xd21>\xf8=\xc6\x84\xfd\xabrs\xc3\xee\xfd+\
w`\x9d\x1a\x0f\xac\x0b\xfe\xf4\x97\xe6l\x1b\x83U\xc1\
\xab\xf6oR2\xbd8\xe02j\xfd\xb583\xfc\x0e\
\x04\xac7\x7fui\x14JV\xc2\x1c\xab\xff\xa5\x15\xab\
\xe3\x81=\xdf\xd2\xbf\xd9\x86\xcdV`jq\xeao\x94\
#\x8b\xbeP@\xe6O\xbf\xe9I\x9f\xac?$t\xf0\
\xf1\xbfkb\xf7\x14\x881\xfc\xad\xfc\xc8\xda)\x10g\
\xdc\xfb\xbe\xdd\xf8\xb9\x955aX`\xf8\x19O\x81\xb0\
\xb0\xe4\xb9\x8f\x7f\xe2eV\xc5E\xe2\x0c\xc3\xdf\xd7d\
iM\x7f8\x88\xb0\xf5\x1b\x229Z\xf1\xa6\xc0vi\
\xe0S\xdfT\x94\xc6\xbf/\xf5\xde\xde\xbd,9\x08\x02\
Q\x00\x1d\x95D^\xe3\x98hP\x87\x08\x89\xb1\xa4\xca\
\xff\xff\xc0\xc9zv)_\xa0\xf7\xac\xdc7v5v\
\x83\xa4\xfd\x82)l\x11\xf0\xb8\xc0xG\xc7w\xba\x9c\
\x07Z\x0c\xfcrT~3\xb9\x89\xe0\xd2\xc0\xa8\x0fw\
\xd4cQ\xe7,\xa8\x82P\xe1\xe5\x9f\x9f\xad\x03\xf94\
@\x05\xda\xbd\xcb8g\x01\x9c'#\x196\xfd\x0b\xca\
\xfd^\x03\x8cc\xd4\xe7\xbf\xe3\xac\x01D\x7f5'\xff\
\xd6\x00\xe3;\xbc\xdc\xd3g\x8fJ{\xd31\xa4:C\
\xf47p\xb9\x95\x1e\xec\x0dU\xdd\xa3\xea\xdb\xceI\x8a\
o\xb7\x19\xaa\xab]\xfc\xd4%l\x17\xd3\xc5\xa3[\xdd\
\x18w\x06m>_D\xa6$\xd4\xad\x86\x92\xd2 \xef\
{\xe7!\x0b\xe6\x16\x97\xde\xab\xe6(\xf7\xf9\x05\xe8l\
\x06\xa1\xdcB\x94\x18\x0c\x06;\x03\x105\xf2\xaaS7\
\xa3T_e\x83\xa4\x1f\x96\xa8y\xf2W\x9c\xb8I\x92\
\xf8\xc5\x9f\x08}\xc8\x22\xdb\xca\xb2 ,\xf9(\xee\x8c\
\x14\xa5l-\x22\xbf#?\xb95\xbd\x1c\xbaZh\x12\
3\x95&IB\xdd\x1b}?\xa4\x8a\xc5D\x8b\xba\x1b\
dol\x8e\x22\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\xf6\x07\x08\x8f\x09\xaf;\x88\xd2\xcf\
\x00\x00\x00\x00IEND\xaeB`\x82\
"

qt_resource_name = b"\
\x00\x05\
\x00o\xa6S\
\x00i\
\x00c\x00o\x00n\x00s\
\x00\x10\
\x02K\x81\x82\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\
\x00\x04\
\x00\x06\xc4\xee\
\x00i\
\x001\x008\x00n\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x0a\
\x03\xd6;g\
\x00M\
\x00a\x00i\x00n\x00W\x00i\x00n\x00d\x00o\x00w\
\x00\x18\
\x0e\x15\xfb\xa3\
\x00b\
\x00r\x00.\x00c\x00o\x00m\x00.\x00j\x00u\x00s\x00t\x00c\x00o\x00d\x00e\x00.\x00Q\
\x00t\x00.\x00e\x00n\x00_\x00U\x00S\
\x00\x10\
\x03\xfa\xc7D\
\x00a\
\x00p\x00p\x00l\x00i\x00c\x00a\x00t\x00i\x00o\x00n\x00-\x00e\x00x\x00i\x00t\
\x00\x12\
\x04\xac\xff\x84\
\x00b\
\x00r\x00.\x00c\x00o\x00m\x00.\x00j\x00u\x00s\x00t\x00c\x00o\x00d\x00e\x00.\x00Q\
\x00t\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00D\x00\x02\x00\x00\x00\x01\x00\x00\x00\x08\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x006\x00\x02\x00\x00\x00\x01\x00\x00\x00\x07\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x05\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8f\x971\xb9\x96\
\x00\x00\x00\x9e\x00\x00\x00\x00\x00\x01\x00\x00\x0bE\
\x00\x00\x01\x8f\x95\xe4 \xef\
\x00\x00\x00\xc4\x00\x00\x00\x00\x00\x01\x00\x00\x0d\x12\
\x00\x00\x01\x8f\x95\xe4 \xef\
\x00\x00\x00h\x00\x00\x00\x00\x00\x01\x00\x00\x08h\
\x00\x00\x01\x8f\x97H}O\
\x00\x00\x00N\x00\x00\x00\x00\x00\x01\x00\x00\x00\x1c\
\x00\x00\x01\x8f\x97?\xcd\x87\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

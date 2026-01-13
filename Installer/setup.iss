; Script de Instalador para Gerador de Voz

[Setup]
AppName=Gerador de Voz
AppVersion=1.0
WizardStyle=modern
DefaultDirName={pf}\GeradorVoz
DefaultGroupName=Gerador de Voz
OutputDir=.
OutputBaseFilename=Instalador_GeradorVoz
SetupIconFile=TTS_GENERATOR.ico
UninstallDisplayIcon={app}\Gerador.exe
Compression=lzma2
SolidCompression=yes

[Files]
Source: "Gerador.exe"; DestDir: "{app}"; Flags: ignoreversion
; Source: "audios\*"; DestDir: "{app}\audios"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{commondesktop}\Gerador de Voz"; Filename: "{app}\Gerador.exe"; IconFilename: "{app}\Gerador.exe"
Name: "{group}\Gerador de Voz"; Filename: "{app}\Gerador.exe"; IconFilename: "{app}\Gerador.exe"

[Run]
Filename: "{app}\Gerador.exe"; Description: "Executar após instalação"; Flags: nowait postinstall skipifsilent

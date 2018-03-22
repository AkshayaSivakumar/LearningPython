import filecmp

dir1 = r'F:\Workspace\Analysis\KETAnalysis\app\src\main\res\drawable-xxhdpi'
dir2 = r'F:\Workspace\KETMobileGit\app\src\main\res\drawable-xxhdpi'

dc = filecmp.dircmp(dir1, dir2).report()
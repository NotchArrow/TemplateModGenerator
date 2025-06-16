import os
import shutil
import time
import ModMakerUtils


# info gathering
modName = input("Enter the name of the mod (Ex: Enchantments Unbound): ")
modVersion = input("Enter the mod version (Ex: 1.21.5): ")

modEnvironment = input("Enter the mod environment (c = client, s = server): ").lower()
while (modEnvironment not in ["client", "main"]):
	if (modEnvironment == "c"):
		modEnvironment = "client"
	elif (modEnvironment == "s"):
		modEnvironment = "main"
	else:
		modEnvironment = input("Enter the mod environment (c = client, s = server): ").lower()

modID = (modName.replace(" ", "-")).lower()
moddingAuthor = ModMakerUtils.moddingAuthor
moddingPackage = ModMakerUtils.moddingPackage

# folder creation
os.mkdir(modID)

# copying of all files that do not need modification from the base template
shutil.copy("template/.gitattributes", f"{modID}/.gitattributes")
shutil.copy("template/.gitignore", f"{modID}/.gitignore")
shutil.copy("template/gradlew", f"{modID}/gradlew")
shutil.copy("template/gradlew.bat", f"{modID}/gradlew.bat")
shutil.copy("template/LICENSE", f"{modID}/LICENSE")
shutil.copy("template/settings.gradle", f"{modID}/settings.gradle")
shutil.copytree("template/gradle", f"{modID}/gradle")
shutil.copytree("template/.github", f"{modID}/.github")

# gradle.properties
versionInfo = ModMakerUtils.getVersionInfo(modVersion)

yarnMappings = versionInfo[1].split("=")[1]
loaderVersion = versionInfo[2].split("=")[1]
loomVersion = versionInfo[3].split("=")[1]
fabricVersion = versionInfo[6].split("=")[1]

file = open("template/gradle.properties", "r")
gradleProperties = file.read()
file.close()

gradleProperties = gradleProperties.replace("1.21.5+build.1", yarnMappings)
gradleProperties = gradleProperties.replace("0.16.14", loaderVersion)
gradleProperties = gradleProperties.replace("1.10-SNAPSHOT", loomVersion)
gradleProperties = gradleProperties.replace("0.127.0+1.21.5", fabricVersion)
gradleProperties = gradleProperties.replace("1.21.5", modVersion)
gradleProperties = gradleProperties.replace("com.example", moddingPackage)
gradleProperties = gradleProperties.replace("template-mod", modID)

file = open(f"{modID}/gradle.properties", "w")
file.write(gradleProperties)
file.close()

# make remaining folders
folders = (moddingPackage + "." + modID.replace("-", "")).replace(".", "/")
os.makedirs(f"{modID}/src/{modEnvironment}/java/{folders}/mixin")
os.makedirs(f"{modID}/src/{modEnvironment}/resources/assets/{modID}")

# fabric.json
file = open("template/src/main/resources/fabric.mod.json", "r")
fabricJson = file.read()
file.close()

fabricJson = fabricJson.replace("Template Mod", modName)
fabricJson = fabricJson.replace("Me!", moddingAuthor)
fabricJson = fabricJson.replace("CC0-1.0", "MIT")
fabricJson = fabricJson.replace("template-mod", modID)
fabricJson = fabricJson.replace("main", modEnvironment)
fabricJson = fabricJson.replace("TemplateMod", modName.replace(" ", ""))
fabricJson = fabricJson.replace("0.16.14", loaderVersion)
fabricJson = fabricJson.replace("1.21.5", modVersion)

file = open(f"{modID}/src/{modEnvironment}/resources/fabric.mod.json", "w")
file.write(fabricJson)
file.close()


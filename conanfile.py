from conans import ConanFile, AutoToolsBuildEnvironment, tools

class PcapplusplusConan(ConanFile):
    name = "PcapPlusPlus"
    version = "v17.11"
    license = "Apache 2.0"
    url = "https://github.com/AndreyBronin/conan-PcapPlusPlus"
    description = "Conan package for PcapPlusPlus"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "libpcap/1.8.1@uilianries/stable"

    def source(self):
        git = tools.Git(folder="PcapPlusPlus")
        git.clone("https://github.com/echo-Mike/PcapPlusPlus.git", "feature/build_system_rework")


    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
	libpcap_info = self.deps_cpp_info["libpcap"]
        include_path = libpcap_info.include_paths[0]
	lib_path = libpcap_info.lib_paths[0]

        with tools.chdir("PcapPlusPlus"):
            self.run("./configure-linux.sh --default")
            build_flags = '-I%s' % include_path
            build_flags += ' -L%s' % lib_path
	    self.run("make -e PCAPPP_BUILD_FLAGS='%s' libs -j5" % build_flags)
#            env_build.make(args=["make -e PCAPPP_BUILD_FLAGS='%s' libs -j5" % build_flags])


    def package(self):
        self.copy("*.h", dst="include", src="PcapPlusPlus/Dist/header")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

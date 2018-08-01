from conans import ConanFile, AutoToolsBuildEnvironment, tools

class PcapplusplusConan(ConanFile):
    name = "PcapPlusPlus"
    version = "latest"
    license = "Apache 2.0"
    url = "https://github.com/AndreyBronin/conan-PcapPlusPlus"
    description = "Conan package for PcapPlusPlus"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "libpcap/1.9.0@andreybronin/stable"

    def source(self):
        #git = tools.Git(folder="PcapPlusPlus")
        self.run("git clone --depth 1 https://github.com/seladb/PcapPlusPlus.git")

    def build(self):
        libpcap_info = self.deps_cpp_info["libpcap"]
        include_path = libpcap_info.include_paths[0]
        lib_path = libpcap_info.lib_paths[0]
        with tools.chdir("PcapPlusPlus"):
            if self.settings.os == "Linux":
                self.run("./configure-linux.sh --default")
            elif self.settings.os == "Macos":
                self.run("./configure-mac_os_x.sh --default")
            elif self.settings.os == "Windows":
                raise ConanException("Windows is not supported yet")
            else:
                raise ConanException("%s is not supported" % self.settings.os)

            build_flags = '-I%s' % include_path
            build_flags += ' -L%s' % lib_path
            self.run("make -e PCAPPP_BUILD_FLAGS='%s' libs -j5" % build_flags)

    def package(self):
        self.copy("*.h", dst="include", src="PcapPlusPlus/Dist/header")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Packet++", "Pcap++", "Common++"]


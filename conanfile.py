from conans import ConanFile

class HelloConan(ConanFile):
    name = "hello"
    url = "abba"
    # version = "0.1"
    def set_version(self):
        version="0.1"
        self.version = version.strip()

    def init(self):
        # self.description = data["description"]

        # https://docs.conan.io/1/mastering/conditional.html
        # check if git-hash not null!
        # if null then ""
        self.url = "yo"

    def package(self):
        # self.configure()
        # self.set_url()
        self.copy("*.m", src="src", keep_path=False)
        # url = ("https://<someurl>/downloads/hello_binary%s_%s.zip"
                #    % (str(self.settings.compiler.version), str(self.settings.build_type))) 


# https://docs.conan.io/1/reference/conanfile/methods.html#init
# https://docs.conan.io/1/howtos/capture_version.html

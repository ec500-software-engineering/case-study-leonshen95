# Case-study: TensorFlow (by Leyang Shen)
## Technology and Platform used for development:
### 1. Language: 
- Tensorflow itself is a deep learning engine open sourced by Google. It was built with the C++ programming language. But in developing applications for this AI engine, coders can use either C++ or Python, the most popular language among deep learning researchers. The hope, however, is that outsiders will expand the tool to other languages, including Google Go, Java, and perhaps even Javascript, so that coders have more ways of building apps. In my opinion, I would choose to use Python for Tensorflow if starting today. Becuase Python is more acceptable and popular and much easier to comprehend nowadays. As Python is covered in most technology fields, I think it would also be easier to integrate different development tools if Tensorflow was built in Python.
### 2. Build System and Build Tools/environment:
- Tensorflow was originally created as an project at Google used by other internal teams, and Google uses a [monolithic repository](https://www.wired.com/2015/09/google-2-billion-lines-codeand-one-place/), in which all projects and all of their dependencies are built using the system on which Bazel is based (Bazel was designed to fit the way software is developed at Google...). As a result, users were able to take the existing BUILD files from their internal version, and—with a small amount of automatic modification—turn them into BUILD files that Bazel understands. There are some platforms that Bazel does not currently serve. So some [Makefiles](https://github.com/tensorflow/tensorflow/tree/7df9c6860e00b91eda0e550b11d9be52d9341d85/tensorflow/contrib/makefile) are made to cross-compile Tensorflow of iOS and Windows.

#### Build from source
- Build from source is available in Linux/macOS, Windows and Raspberry Pi. 

- User needs to install Python and Tensorflow package dependencies, install Bazel, install GPU support(optional), donwload the tensorflow source code. Configure the build, build the pip package, Docker Linux builds and Tested build configurations. The build details is attached:

[Build from source(Linux/macOS)](https://www.tensorflow.org/install/source)

[Build from source(Windows)](https://www.tensorflow.org/install/source_windows)

[Build from source(Raspberry Pi)](https://www.tensorflow.org/install/source_rpi)

- Tensorflow also provides different languages API - particular useful for loading models created with Python and running them within a different languages application.

[JAVA API](https://www.tensorflow.org/install/lang_java)

[C API](https://www.tensorflow.org/install/lang_c)

[GO API](https://www.tensorflow.org/install/lang_go)

#### What is special about Bazel that Google has to use it to develop Tensorflow?
- Multi-language support: Bazel supports Java, Objective-C and C++ out of the box, and can be extended to support arbitrary programming languages.

- High-level build language: Projects are described in the BUILD language, a concise text format that describes a project as sets of small interconnected libraries, binaries and tests. In contrast, with tools like Make, you have to describe individual files and compiler invocations.

- Multi-platform support: The same tool and the same BUILD files can be used to build software for different architectures, and even different platforms. At Google, we use Bazel to build everything from server applications running on systems in our data centers to client apps running on mobile phones.

- Reproducibility: In BUILD files, each library, test and binary must specify its direct dependencies completely. Bazel uses this dependency information to know what must be rebuilt when you make changes to a source file, and which tasks can run in parallel. This means that all builds are incremental and will always produce the same result.

- Scalable: Bazel can handle large builds; at Google, it is common for a server binary to have 100k source files, and builds where no files were changed take about ~200ms.

### 3. Framework/libraries
- The framework for Tensorflow is known for having an architecture that allows computation on any CPU or GPU, be it a desktop, a server, or even a mobile device. This framework is available in the Python programming language. The advantage of using this framwork is 1. Uses an easy-to-learn a language (Python);2. Uses computational graph abstraction;3. Availability of TensorBoard for visualization.



Reference:
https://www.wired.com/2015/11/google-open-sources-its-artificial-intelligence-engine/
https://www.quora.com/Why-did-Google-decide-to-use-Bazel-with-TensorFlow
https://bazel.build/faq.html#what-is-special-about-bazel

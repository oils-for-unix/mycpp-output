mycpp-output
============

This repository stores files generated from the main Oils repo:

    https://github.com/oils-for-unix/oils

When changing mycpp, it's useful to diff against these "golden" files.

Note: we could also store the whole tarball, including ASDL ...

---

Right now, I update the files like this:

    ./run.sh update-from-tarball

This builds the tarball and `mycpp/examples` from the `oils` repo, and copies
the generated code into this repo.

   

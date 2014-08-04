Title:   Introducing HippyVM
Date:    24-03-2014
url:     introducing-hippyvm

We're pleased to introduce a pre-release of our new implementation
of the [PHP](http://php.net) language,
HippyVM. This website is dedicated to the ongoing effort of building
a high-performance virtual machine based on the technology built for
a fast Python virtual machine, the [PyPy project](http://pypy.org).

What's HippyVM?
---------------

HippyVM is a reimplementation of the PHP language using PyPy technology.
It started off as a [research project done for facebook](http://morepypy.blogspot.com/2012/07/hello-everyone.html) by Maciej Fijałkowski,
and was later expanded. Right now it contains a fast and reasonably complete
implementation of the core PHP language. It also includes implementations of
many PHP built-in modules, but far from all of them. As of now it does not include
web server integration, so it is not yet suitable for use in production.

How fast is it?
---------------

We have gathered a set of small benchmarks to test the performance of our virtual
machine. We're in the process of gathering more application-size benchmarks
like mediawiki or wordpress. We'll post them as soon as possible.

Current status can be seen in
[the performance section](http://hippyvm.com/#performance) of our website, which currently
contains only small-to-medium size microbenchmarks that we
could find or reasonably implement. Right now, HippyVM is **7.3x faster** than stock
PHP and **2x faster** than [HHVM](http://hhvm.com/), using a geometric mean.
Please note that these benchmarks might not be representative, and consult
specific benchmarks as they vary widely.

Is this Open Source?
--------------------

[The pre-release](http://github.com/hippyvm/hippyvm)
is open source, but we plan to sell a commercial version
in the future. We will have a model where the core language as
well as core JIT technologies remain Open Source, while some extension
modules as well as the web server integration are proprietary.

The pre-release is MIT-licensed.

What's included and what's not included in the pre-release?
----------------------------------------------------------

The pre-release includes only the Open Source part of HippyVM. We will make
a commercial pre-release which includes extension modules and web server
integration some time in the next few months.

What are the plans for the future?
----------------------------------

We have a good implementation of the PHP language, but we're missing many
crucial modules. We aim to finish this part later this year. We're also
planning to have a novel bridge which would let you leverage the Python ecosystem
from PHP. Additionally, we're investing ongoing effort into making our JIT
technology even better and making both PyPy and Hippy a lot faster.

Cheers,  
Maciej Fijalkowski and the entire HippyVM team.

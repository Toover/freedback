Freedback White Book
====================

The main principles driving this project are to be found and maintained in this
file.

The vision
----------

Everything deserve feedback! Especially when us, people are impacted. Even
more: it should be required that anything that may impact us provide a way
to collect feedback, a channel.

But we cannot force or wait for every organization to provide such a channel.
Instead, Freedback proposes that people use their own channel!
For our voice to be heard, Freedback proposes a way to collect feedback, so
that platforms can publish them and benefit the organizations, or the users
themselves.

The strategy
------------

The vision cannot be achieved without a critical mass of users and
organizations agreeing upon using Freedback. So maybe the vision will
never be met! However, there are already advantages that justify using
Freedback. The strategy consists simply in focusing on what Freedback can
bring to projects, case by case.

The growth of the project should be driven by the immediate use cases, but
must not compromise the vision. To achieve this, libraries and applications
should be developed, but the protocol and specifications must remain stable.

Use cases
---------

As a consumer, I have access to a mobile application that allows me to provide
feedback without subscription on:

- products I consume, identified with barcodes

- websites I visit, identified with URLs

- applications installed from sources that do not propose comments like F-Droid

As consumer organization, I can discover all the sources of feedback that
are public and collect the feedback data from them. I can publish and store
anonymized data and analyze it.

As an application provider, my clients can provide feedback about my service
directly from the application, and I can choose whether to keep the data
private or publish it. I can reply back to clients to provide help if they
accept to.

As a Freedback user, I do not need to set up a server nor to rely on a
centralized instance. I can choose how the data is stored and distributed.

As a social being, I want to choose whether to show my identity or not in some
feedback. In any case, I can accept or not to be replied to. I can also discuss
other feedback entries by replying to them. I may want to keep my identity
consistent accross devices and in time.

What Freedback is
-----------------

Before anything, Freedback is a specification and a protocol for representing
and communicating feedback about anything that has an identity. To ensure
a minimal support, the Freedback project may include:

- a library to embed in applications that desire to use Freedback

- a library to collect Freedback entries into databases and for analysis

- a client application for mobile users to provide feedback IRL

- a server application to collect and publish the data provided by clients

- examples to get up-to-speed for using Freedback directly from existing
  applications

Freedback is free as in freedom, and can be used anywhere with a
non-contaminating license. It is encouraged to produce data with 

As standard as possible
-----------------------

When choosing a solution for an interface or for an implementation, always:

- consider existing alternatives

- prefer standard alternatives by default

- for standards, the newer the better, by default

Examples of standards: RFCs, ISO, IPv6, HTTP, C++ STL, Docker...

Quality level
-------------

Testability is a requirement to any piece of software. As many features
and fixes as possible must be proven using automated tests. Any untested
feature is a risk for the reliability of the software. Unreliable software
is unattractive and not suitable for industries. High reliability is a
requirement for the long-term vision.

Reliability not only concerns the software, but the project itself. Accidents
always happen in projects, and damage can be controlled when good maintenance
practices at respected: specification, review, testing, documentation, code
consistency and expressivity are examples of the good practices required to
build the reliability of the project in the long-term.

Using Freedback in Freedback
----------------------------

Though the core of the development process should not depend on Freedback, the
software delivered to use Freedback should also use Freedback to provide
feedback about the project. For example, the client application should let user
produce feedback on the application itself. Using what we produce forces us to
see it, and be more critical about it.

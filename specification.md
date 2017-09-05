Freedback Specifications
========================

Protocol Layers
---------------

Freedback must work over the Internet, and must therefore support the IP.
It allows the broadest availability of Freedback services. For reliability
reasons, the support of TCP is required. Any hardware bus supporting the
TCP/IP layers is suitable for Freedback. For the application layer to be
accepted for most clients, HTTP protocols are preferred. For obvious privacy
reasons, the content of the HTTP requests should be encrypted, for example
using SSL.

The newest standard to match this spec would be SSL-encrypted HTTP/2 over
TCP/IPv6. Consider REST APIs or gRPC, for example.

Protocol Negotiation
--------------------

There is no good reason the initial specifications of the protocol would
be good enough for the long run. As a consequence, the protocol should
expect to exist in several versions. Clients and server must therefore
agree on which version of the protocol they will be using.

Since the communication is at the initiative of the client, it is the client
that must make sure that it is using a compatible protocol. It should be done
with a request to the server which result consists in ranges of supported
protocols. The client can and should find by itself the highest version that
is supported by both parties.

It is also expected that options may enable special communication modes.
These options must be negotiated too, so that only the supported options
should be used. Every client or service supporting a version of the protocol
must at least support it without option, because peer may not agree on options.

When the next requests are made from a client to a server, they must both know
in which version of the protocol is used. It should be supported that this
information can be found in every single request, at least. Optimizations
are possible if sessions can be opened and used.

Service Discovery
-----------------

It must be decentralized and robust to being abandoned by the project
maintainers. The services themselves should be able to guarantee it keeps
on working. DHT is a good tool for implementing a distributed directory,
and is resilient. The distributed data should be as light as possible, and
only helps clients to find the root URL of the services.

This root URL is a requirement to resolve the REST API of the service. The
API may change in time, so the service should announce the version of that
API when querying the root URL. With the root URL, the API version and the
history of the APIs specified by the project, it should be possible for a
client use the target service fully.

The API specification must therefore be formalized in a way to make it
programmatically inspectable, so that we can assert the suitability of the
client code.

Authentication
--------------

In some cases, a Freedback service may limit its access to recognized users.
Authentication is therefore required, and may have an impact in every request
between the client and the server. Authentication is to be handled by the
service provider, but the Freedback protocol must allow arbitrary
authentication data in the messages. It must be specified how authentication
is meant to work, with the help of practicle examples.

Providing Feedback
------------------

This is the most important part. A single REST endpoint should allow to input
a feedback entry. A feedback entry consists in at least an identifiable
subject, an identifiable feedback provider and the feedback content. Various
types of feedback contents may exist and appear in the future. For example: 
"comment", "rating" or "issue". Each type of feedback is associated with some
data type. The data types are to be specified and respected. Unknown, new,
data types can be used freely, but services must warn, if some data could not
be processed.

Storing Feedback
----------------

Feedback can be of various, unexpected types. It is important that the
server library suggests a default data storage that supports unexpected
types. But it must remain an optional helper. Various connectors should be
supported so that service providers can choose the database implementation
they want.

The information always consists in the following relation: a user provided
some a feedback about a subject. The feedback is regroups a set of
arbitrarily typed feedback data.

Retrieving Feedback
-------------------

It is up to the service provider to choose whether and how to distribute the
data. Freedback cannot force the data to be published, but it should provide
a default mechanism, as an incentive to share data, the Open Data way.

The focus of Freedback is to provide feedback on a subject, not to track the
user behavior! So the recommended query API consists in:

- providing a listing of the subjects

- for a set of subjects, retrieve all feedbacks

- for a set of subjects, retrieve feedbacks in a given set of types

Data Distribution Policies
--------------------------

The data collected by Freedback must always come along with licensing
information. The client applications must specify explicitly the associated
licensing information, so that user can be aware of how their data could be
processed. Open Data licensing or Business-alike Creative Commons are the most
permissive license, and should be proposed by default.

The licensing information must be made available on a specific endpoint, that
and has a contractual value for both collecting and publishing. The supported
licence strings need to be specified, so that feedback miners can filter out
data depending on the licensing.

According to laws and regulations (citations needed), users retain full control
on their data and can view, modify and delete pieces or all of it. As a
consequence, the system should enforce a way for clients to alter the entries
they provided.

Subject, User and Type Identification
-------------------------------------

It is recommended that a subject is an URI, like specified in RDF. Users too,
but they often are anonymous. In that case, UUIDs should be supported. Type
identification should be specified as an URI too, like predicates are specified
in RDF.

API Specification
-----------------

It is a file found:

- In the sources of Freedback

- In any binary distribution

- Online in the documentation of Freedback

It holds the information of since when an API was specified, and when it was
deprecated or removed. It should be easy to parse to figure out what is the
current API. It should be programmatically readable so that to show the
available API for given version ranges.

API version is an integer that is incremented whenever a set of API changes, in
the spirit of continuous release.

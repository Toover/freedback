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
TCP/IPv6. The current standard for web APIs is REST, where structured data
is exchanged in HTTP requests to specified URLs.

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

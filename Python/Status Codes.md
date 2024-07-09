Common HTTP status codes along with their definitions:

### Informational Responses
- **100 Continue**: The server has received the request headers and the client should proceed to send the request body.
- **101 Switching Protocols**: The requester has asked the server to switch protocols, and the server has agreed to do so.
- **102 Processing**: The server has received and is processing the request, but no response is available yet.

### Successful Responses
- **200 OK**: The request was successful.
- **201 Created**: The request was successful and a new resource was created.
- **202 Accepted**: The request has been accepted for processing, but the processing has not been completed.
- **203 Non-Authoritative Information**: The request was successful but the returned meta-information is from a local or third-party copy, not from the origin server.
- **204 No Content**: The server successfully processed the request, but is not returning any content.
- **205 Reset Content**: The server successfully processed the request, but is not returning any content and requires that the requester reset the document view.
- **206 Partial Content**: The server is delivering only part of the resource due to a range header sent by the client.

### Redirection Messages
- **300 Multiple Choices**: There are multiple options for the resource that the client may follow.
- **301 Moved Permanently**: The URL of the requested resource has been changed permanently.
- **302 Found**: The URL of the requested resource has been changed temporarily.
- **303 See Other**: The server sent this response to direct the client to get the requested resource at another URI with a GET request.
- **304 Not Modified**: This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.
- **305 Use Proxy**: The requested resource is available only through a proxy, the address for which is provided in the response.
- **307 Temporary Redirect**: The server is currently responding to the request with a resource from a different URI, but the client should use the original URI for future requests.
- **308 Permanent Redirect**: The resource is now permanently located at another URI.

### Client Error Responses
- **400 Bad Request**: The server could not understand the request due to invalid syntax.
- **401 Unauthorized**: The client must authenticate itself to get the requested response.
- **402 Payment Required**: This response code is reserved for future use.
- **403 Forbidden**: The client does not have access rights to the content.
- **404 Not Found**: The server can not find the requested resource.
- **405 Method Not Allowed**: The request method is known by the server but is not supported by the target resource.
- **406 Not Acceptable**: The server can only generate a response that is not accepted by the client.
- **407 Proxy Authentication Required**: The client must first authenticate itself with the proxy.
- **408 Request Timeout**: The server would like to shut down this unused connection.
- **409 Conflict**: This response is sent when a request conflicts with the current state of the server.
- **410 Gone**: The content requested has been permanently deleted from the server, with no forwarding address.
- **411 Length Required**: The server rejected the request because the Content-Length header field is not defined and the server requires it.
- **412 Precondition Failed**: The client has indicated preconditions in its headers which the server does not meet.
- **413 Payload Too Large**: The request entity is larger than limits defined by the server.
- **414 URI Too Long**: The URI requested by the client is longer than the server is willing to interpret.
- **415 Unsupported Media Type**: The media format of the requested data is not supported by the server.
- **416 Range Not Satisfiable**: The range specified by the Range header field in the request can't be fulfilled.
- **417 Expectation Failed**: The server cannot meet the requirements of the Expect request-header field.
- **418 I'm a teapot**: This code was defined in 1998 as one of the traditional IETF April Fools' jokes.
- **421 Misdirected Request**: The request was directed at a server that is not able to produce a response.
- **422 Unprocessable Entity**: The request was well-formed but was unable to be followed due to semantic errors.
- **423 Locked**: The resource that is being accessed is locked.
- **424 Failed Dependency**: The request failed due to failure of a previous request.
- **425 Too Early**: Indicates that the server is unwilling to risk processing a request that might be replayed.
- **426 Upgrade Required**: The client should switch to a different protocol.
- **428 Precondition Required**: The origin server requires the request to be conditional.
- **429 Too Many Requests**: The user has sent too many requests in a given amount of time.
- **431 Request Header Fields Too Large**: The server is unwilling to process the request because its header fields are too large.
- **451 Unavailable For Legal Reasons**: The user requests an illegal resource, such as a web page censored by a government.

### Server Error Responses
- **500 Internal Server Error**: The server has encountered a situation it doesn't know how to handle.
- **501 Not Implemented**: The request method is not supported by the server and cannot be handled.
- **502 Bad Gateway**: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
- **503 Service Unavailable**: The server is not ready to handle the request.
- **504 Gateway Timeout**: The server is acting as a gateway or proxy and did not receive a timely response from the upstream server.
- **505 HTTP Version Not Supported**: The HTTP version used in the request is not supported by the server.
- **506 Variant Also Negotiates**: The server has an internal configuration error.
- **507 Insufficient Storage**: The server is unable to store the representation needed to complete the request.
- **508 Loop Detected**: The server detected an infinite loop while processing the request.
- **510 Not Extended**: Further extensions to the request are required for the server to fulfill it.
- **511 Network Authentication Required**: The client needs to authenticate to gain network access.

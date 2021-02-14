# Working with GitHub v4 GraphQL API

GraphApi class contains method for getting all release tags for a certain repository
and getting download url for certain release.

## Usage

### Instantiate
`api = GraphqlApi(url, auth)`
auth is the personal aceess token provided by GitHub. It can be used as bearer token.
Example: 'token token12345token12345'

### getUrlByTag
`api.getUrlByTag(tag)`
get download url for release, by using release tag as the parameter

### getAllTags
`api.getAllTags()`
get first 100 tags for a repository as a list
def getQueryForTag(tag):
    query = """
        {
            repository(owner:"erlang",name:"otp"){
                id
                release(tagName:"%s"){
                releaseAssets(first:100){
                    nodes{
                        name
                        downloadUrl
                    }
                }
            }
        }
    }
    """ %(tag)
    return query

def getAll():
    query = """
        {
            repository(owner:"erlang",name:"otp"){
                id
                releases(orderBy:{direction:DESC,field:NAME},first:100){
                    nodes{
                        url
                        tag{
                            name
                        }
                    }
                }
            }
        }
        """
    return query
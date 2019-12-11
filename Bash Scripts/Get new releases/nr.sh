#!/bin/bash
# gets 50 albums new released 1 at a time
token='BQCa3HEoIUYVbM4I0wFhJ50wj8mU3akh07VFpN4zv5NtDW-miYORdRXT-PC-GEv4xfDEnOV4qKBVZf91hpbZQsFVDyrFRINGSGRh-vbh4r3eUCF21_panWRVY34tZDmvfAjyJlnXCh0LRr6geM_N7ukVTPYyZwc'
init=0
limit=1
for i in {1..50}; do
    let start=init+i
    file_out="new_album_${start}.json"

    curl -X "GET" "https://api.spotify.com/v1/browse/new-releases?limit=${limit}&offset=${start}"\
    -H "Accept: application/json" -H "Content-Type: application/json"\
      -H "Authorization: Bearer ${token}" >> $file_out

    echo $i
    echo $file_out

done


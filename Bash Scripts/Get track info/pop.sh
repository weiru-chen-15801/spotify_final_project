#!/bin/bash
#reads a list of lists of track ids and downloads json files with track features for each track list
playlists='playlists.txt'
count=1
while read pl; do
    file_in=$pl
    file_out="track_info_${count}.json"
    token='BQDO81VpwIguEc1AP2vN9XfY8zdLjBCFF62pvCb9g70HCTkgjrNZ8oPbK04c0L5EwlO3wEQ9cPjm1Z__z6Qqi_UFQMuCjSw_xyrYOFtsJvwvwgFdwPo9-jwIoWEG7ASU4RdU1yy-AGAvmTyNcMpbGVIzKynGAzg'
    tracks=''

    p=0
    while read line; do
        tracks+=$line
        tracks+="%2C"
        p=$((p+1))
        echo $p
        if [ $p -eq 50 ]; then
            break
        fi
    done < $file_in

    tracks=${tracks%???}


    curl -X "GET" "https://api.spotify.com/v1/tracks?ids=${tracks}"\
    -H "Accept: application/json" -H "Content-Type: application/json"\
    -H "Authorization: Bearer ${token}" >> $file_out

    echo $count
    echo $file_in
    echo $file_out
    count=$((count+1))
done < $playlists

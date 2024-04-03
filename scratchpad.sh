#!/usr/bin/env bash

pretty(){
  python3 -mjson.tool
}

diffs(){
  curl -s "https://www.courts.mo.gov/cnet/cases/newHeaderData.do?caseNumber=171155061&courtId=CT12&isTicket=&locnCode=" | pretty > sample1.json
  curl -s 'https://www.courts.mo.gov/cnet/cases/party.do?caseNumber=171155061&courtId=CT12&isTicket=' | pretty > sample2.json

  diff sample1.json sample2.json
}


do_curl(){
  curl 'https://www.courts.mo.gov/cnet/searchResult.do' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'Accept-Language: en-US,en;q=0.9' \
    -H 'Connection: keep-alive' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Cookie: JSESSIONID=0001yGlh_32octySxyI-U7tSOZQ:-1PCB; JSESSIONID=0001ZU-jb8qmlZ1dV_djDNm_RMa:-1088NE7; visitorid=20240402143553887447; UJID=f2d0c9e2-719e-4080-802e-64f5cce3272e; UJIA=-1951283160; _gid=GA1.2.663357942.1712086557; _gat_gtag_UA_109681667_1=1; _ga_DSVJ8DTRVZ=GS1.1.1712149531.3.1.1712149531.0.0.0; _ga=GA1.1.244685733.1712086557' \
    -H 'Origin: https://www.courts.mo.gov' \
    -H 'Referer: https://www.courts.mo.gov/cnet/searchResult.do?countyCode=WRN&newSearch=Y&courtCode=CT12&startDate=03%2F24%2F2024&caseStatus=A&caseType=Traffic%2FMunicipal&locationCode=' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'sec-ch-ua: "Not(A:Brand";v="24", "Chromium";v="122"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Linux"' \
    --data-raw '{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"initFiling","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseNumber","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseStyle","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseType","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"countyDesc","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}}],"order":[{"column":0,"dir":"asc"}],"start":0,"length":10,"search":{"value":"","regex":false}}'
}


do_curl_simple(){
curl 'https://www.courts.mo.gov/cnet/searchResult.do' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Cookie: JSESSIONID=0001fIJANtS3FyFj3q6o-iLrDGv:1NJUVVVENT;' \
  --data-raw '{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"initFiling","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseNumber","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseStyle","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseType","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"countyDesc","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}}],"order":[{"column":0,"dir":"asc"}],"start":0,"length":10,"search":{"value":"","regex":false}}'
}

do_curl_2(){
  curl 'https://www.courts.mo.gov/cnet/searchResult.do' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Cookie: JSESSIONID=00018AyD23UHxgAHrkgrArPuQsz:-1PCB;' \
    --data-raw '{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"initFiling","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseNumber","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseStyle","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"caseType","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}},{"data":"countyDesc","name":"","searchable":true,"orderable":true,"search":{"value":"","regex":false}}],"order":[{"column":0,"dir":"asc"}],"start":0,"length":10,"search":{"value":"","regex":false}}'
}

#do_curl_simple
do_curl_2
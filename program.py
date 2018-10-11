vzorec = (
    #leto začetka predstave
    r'</td><td data-label="" class="col-1"><a  href="/production/\w+(P<year>\d{4})"'
    #naslov predstave
    r'title data-cms-ai="0" >(P<show>\w+))</a>'
    #prizorišče predstave
    r'</td><td data-label="" class="col-2">(P<venue>\w+))</td>'
    #žanr predstave
    r'<td data-label="" class="col-3">(P<genre>\w+)</td>
    #mesto predstave
    r'<td data-label="" class="col-4">(P<location>\w+ , \w\w)</td>'
    #tip predstave
    r'<td data-label="" class="col-5">(P<type>\w+)</td>'
)
from sec_edgar_downloader import Downloader

dl = Downloader("Bridget Leonard", "leonardbridget01@gmail.com",
                "sec-edgar-downloader/filing_results")

# Get most recent 10-K for nvda
dl.get("10-K", "NVDA", limit=1)

# Get the latest supported filings, if available, for Nvidia
for filing_type in dl.supported_filings:
    dl.get(filing_type, "NVDA", limit=1)

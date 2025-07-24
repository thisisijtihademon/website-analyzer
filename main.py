# main.py
from crawler import crawl_website
from analyzer import analyze_page
from report_generator import save_report

if __name__ == "__main__":
    website = input("Enter full website URL (with https://): ").strip()
    pages = crawl_website(website)

    all_data = []
    for url, html in pages:
        print(f"Analyzing: {url}")
        result = analyze_page(html)
        result['url'] = url
        all_data.append(result)

    save_report(all_data)
    print("✅ Analysis complete. Report saved as 'website_report.xlsx'")

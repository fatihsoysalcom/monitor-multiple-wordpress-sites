import urllib.request
import re
import ssl

def get_wp_version_and_status(url):
    """
    Fetches the homepage of a WordPress site and attempts to extract
    its version from the generator meta tag, and reports HTTP status.
    """
    try:
        # Create an unverified SSL context for demonstration purposes.
        # In production, proper certificate validation is crucial.
        context = ssl._create_unverified_context()

        with urllib.request.urlopen(url, timeout=10, context=context) as response:
            status_code = response.getcode()
            html_content = response.read().decode('utf-8', errors='ignore')

            # Regex to find the WordPress generator meta tag
            # Example: <meta name="generator" content="WordPress 6.4.3" />
            match = re.search(r'<meta name="generator" content="WordPress ([\d.]+)"', html_content)
            if match:
                wp_version = match.group(1)
            else:
                wp_version = "Not Found (meta tag)"

            return status_code, wp_version
    except urllib.error.HTTPError as e:
        return e.code, "Error (HTTP)"
    except urllib.error.URLError as e:
        return "N/A", f"Error (URL: {e.reason})"
    except Exception as e:
        return "N/A", f"Error (General: {e})"

if __name__ == "__main__":
    # List of WordPress site URLs to monitor.
    # This demonstrates how a custom script can centralize and automate checks.
    wordpress_sites = [
        "https://wordpress.org",         # A known WordPress site
        "https://example.com",           # Placeholder for a real site
        "https://dev.to",                # A non-WordPress site for comparison
        "https://httpbin.org/status/404", # A site returning 404
        "https://nonexistent-domain-12345.com", # A non-existent domain
        # Add more sites here to simulate managing multiple instances efficiently.
    ]

    print("--- Monitoring WordPress Sites ---")
    print("-" * 30)

    for site_url in wordpress_sites:
        print(f"Checking: {site_url}")
        status, version = get_wp_version_and_status(site_url)

        # The core concept: efficient, automated monitoring of multiple sites.
        print(f"  Status: {status}")
        print(f"  WP Version: {version}")
        print("-" * 30)

    print("--- Monitoring Complete ---")

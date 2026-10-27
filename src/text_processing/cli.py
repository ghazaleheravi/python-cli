import argparse
import urllib.request
import gzip 

def handle_request(url, output_file):
  try:
    # Faking a standard browser layout request
    req = urllib.request.Request(
      url, 
      headers={
        'Accept-Encoding': 'gzip'  # Formally tells the server gzip is supported
      }
    )

    with urllib.request.urlopen(req) as response:
      raw_data = response.read()
      # Check if website wrapped the response in a gzip package
      if response.info().get('Content-Encoding') == 'gzip':
        # Safely unzip the bytes sequence back into regular raw content
        html_bytes = gzip.decompress(raw_data)
      else:
        html_bytes = raw_data

      encoding = response.info().get_content_charset() or 'utf-8'
      decoded_content = html_bytes.decode(encoding)

    if output_file is not None:
      with open(output_file, "w", encoding="utf-8") as file:
        file.write(decoded_content)
      print(f"Successfully saved content to {output_file}")
    else:
      print(decoded_content)    

  except Exception as e:
    print(f"An error occurred: {e}")

def handle_print():
  print('You can do this!')


def cli_example (): 
  # 1. Initialize the parser
  parser = argparse.ArgumentParser(description="Text processing tool.")
  subparsers = parser.add_subparsers(dest='command')

  # 2. Define the arguments you want to accept
  request_parse = subparsers.add_parser('request', help='make a request to a website')
  request_parse.add_argument('website', help='path to website to request')
  request_parse.add_argument('-o', '--output_file', help='where to save the requested page')

  request_parse = subparsers.add_parser('print', help='print a kindly message')


  # 3. Parse the arguments 
  args = parser.parse_args()

  if args.command == 'request':
    handle_request(args.website, args.output_file)
  elif args.command == 'print':
    handle_print()
  else:
    parser.print_help()  


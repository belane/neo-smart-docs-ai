import os
from urllib.parse import urlparse
from llama_index import download_loader, GPTVectorStoreIndex, TrafilaturaWebReader
from llama_hub.github_repo import GithubRepositoryReader, GithubClient
import nest_asyncio
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')
nest_asyncio.apply()
enable_verbose = False

print('# Loading GitHub Client')
download_loader("GithubRepositoryReader")
github_client = GithubClient(github_token=os.environ.get('GITHUB_TOKEN'))
documents = []

print('# Processing Neo documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="docs",
    filter_directories=(["articles", "zh-cn"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if 'zh-cn' in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if doc.extra_info['file_path'] == 'README.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://docs.neo.org/" + doc.extra_info['file_path'].replace('.md','.html').replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing Neo Dev documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="neo-dev-portal",
    filter_directories=(["static", "src", "recipes", "i18n", "zh"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if 'recipes' in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if 'i18n' in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if 'zh' in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if doc.extra_info['file_path'] == 'README.md':
        parsed_docs.remove(doc)
        continue
    if 'tutorials' in doc.extra_info['file_path']:
        doc.extra_info['file_path'] = urlparse("https://developers.neo.org/" + doc.extra_info['file_path'].replace('.md','').replace('\\', '/').replace('-','/',3).replace('/index','')).geturl()
    else:
        doc.extra_info['file_path'] = urlparse("https://developers.neo.org/" + doc.extra_info['file_path'].replace('.md','').replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing Neo Proposals')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="proposals",
    filter_directories=(["obsolete"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".mediawiki"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if doc.extra_info['file_path'] == 'README.mediawiki':
        parsed_docs.remove(doc)
        continue
    if doc.extra_info['file_path'] == 'nep-X.mediawiki':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/neo-project/proposals/blob/master/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neo-mamba documentation')
client = GithubRepositoryReader(
    github_client,
    owner="CityOfZion",
    repo="neo-mamba",
    filter_directories=(["docs"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if doc.extra_info['file_path'] == 'docs\\source\\advanced.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://dojo.coz.io/" + doc.extra_info['file_path'].replace('docs\\source\\', 'neo3/mamba/').replace('.md','.html').replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neow3j documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neow3j",
    repo="neow3j-docs",
    filter_directories=(["docs"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if 'neo-n3' not in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if doc.extra_info['file_path'] == 'docs\\neo-n3\\_sidebar.md':
        parsed_docs.remove(doc)
        continue
    if doc.extra_info['file_path'] == 'docs\\neo-n3\\README.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://neow3j.io/#/" + doc.extra_info['file_path'].replace('docs\\', '').replace('.md','').replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neon-js documentation')
client = GithubRepositoryReader(
    github_client,
    owner="CityOfZion",
    repo="neon-js",
    filter_directories=(["docs"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if 'changelog' in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://dojo.coz.io/" + doc.extra_info['file_path'].replace('docs\\', 'neo3/neon-js/docs/').replace('.md','').replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neo-boa documentation')
doc_urls = [
    'https://dojo.coz.io/neo3/boa/getting-started.html',
    'https://dojo.coz.io/neo3/boa/tutorials.html',
    'https://dojo.coz.io/neo3/boa/conceptual-overview.html',
    'https://dojo.coz.io/neo3/boa/code-reference.html'
]
docs = TrafilaturaWebReader(True).load_data(doc_urls)
# Parse references
for i, doc in enumerate(docs):
    doc.extra_info = { 'file_path': doc_urls[i] }
# Add to document library
documents += docs

print('# Processing neo-go documentation')
client = GithubRepositoryReader(
    github_client,
    owner="nspcc-dev",
    repo="neo-go",
    filter_directories=(["docs"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if doc.extra_info['file_path'] == 'docs\\release-instruction.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/nspcc-dev/neo-go/blob/master/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neofs documentation')
doc_urls = [
    'https://fs.neo.org',
    'https://fs.neo.org/network/',
    'https://fs.neo.org/data/',
    'https://fs.neo.org/audit/',
    'https://fs.neo.org/pricing/',
    'https://fs.neo.org/hosting/',
    'https://neospcc.medium.com/neofs-rest-gateway-4994a8ada04'
]
docs = TrafilaturaWebReader(True).load_data(doc_urls)
# Parse references
for i, doc in enumerate(docs):
    doc.extra_info = { 'file_path': doc_urls[i] }
# Add to document library
documents += docs

print('# Processing NeoLine dAPI documentation')
doc_urls = [
    'https://neoline.io/dapi/N3.html'
]
docs = TrafilaturaWebReader(True).load_data(doc_urls)
# Parse references
for i, doc in enumerate(docs):
    doc.extra_info = { 'file_path': doc_urls[i] }
# Add to document library
documents += docs

print('# Processing WalletConnect SDK documentation')
doc_urls = [
    'https://neon.coz.io/wksdk/core/index.html'
]
docs = TrafilaturaWebReader(True).load_data(doc_urls)
# Parse references
for i, doc in enumerate(docs):
    doc.extra_info = { 'file_path': doc_urls[i] }
# Add to document library
documents += docs
client = GithubRepositoryReader(
    github_client,
    owner="CityOfZion",
    repo="wallet-connect-sdk",
    filter_directories=(["common","packages"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="main")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if doc.extra_info['file_path'] != 'README.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/CityOfZion/wallet-connect-sdk/blob/main/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing Neo modules documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="neo-modules",
    filter_directories=(["test","src"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if doc.extra_info['file_path'] != 'README.md':
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/neo-project/neo-modules/blob/master/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neo-worknet documentation')
client = GithubRepositoryReader(
    github_client,
    owner="N3developertoolkit",
    repo="neo-worknet",
    filter_directories=(["src"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="main")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    doc.extra_info['file_path'] = urlparse("https://github.com/N3developertoolkit/neo-worknet/blob/main/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neo-express documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="neo-express",
    filter_directories=(["src", "deps"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if "changelog.md" in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if "legacy" in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/neo-project/neo-express/blob/master/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Processing neo-debugger documentation')
client = GithubRepositoryReader(
    github_client,
    owner="neo-project",
    repo="neo-debugger",
    filter_directories=(["src"], GithubRepositoryReader.FilterType.EXCLUDE),
    filter_file_extensions=([".md"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=enable_verbose,
    concurrent_requests=10,
)
docs = client.load_data(branch="master")
# Parse references
parsed_docs = docs.copy()
for doc in docs:
    if "CHANGELOG.md" in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    if "legacy" in doc.extra_info['file_path']:
        parsed_docs.remove(doc)
        continue
    doc.extra_info['file_path'] = urlparse("https://github.com/neo-project/neo-debugger/blob/master/" + doc.extra_info['file_path'].replace('\\', '/')).geturl()
    # remove 'file_name' for storage optimization
    del doc.extra_info['file_name']
# Add to document library
documents += parsed_docs

print('# Generate Index storage')
# Construct a simple vector index
index = GPTVectorStoreIndex.from_documents(documents)
# Saving Index for future use
index.storage_context.persist()

print('# Test Index storage')
query_engine = index.as_query_engine()
test_query = "What are scope signatures?"
response = query_engine.query(test_query)
print(test_query, '>>', response)

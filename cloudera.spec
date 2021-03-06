lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'twitter/version'

Gem::Specification.new do |spec|
  spec.add_dependency 'addressable', '~> 2.3'
  spec.add_dependency 'buftok', '~> 0.2.0'
  spec.add_dependency 'equalizer', '~> 0.0.11'
  spec.add_dependency 'http', '~> 0.9.4'
  spec.add_dependency 'http-form_data', '~> 1.0'
  spec.add_dependency 'http_parser.rb', '~> 0.6.0'
  spec.add_dependency 'memoizable', '~> 0.4.0'
  spec.add_dependency 'multipart-post', '~> 2.0'
  spec.add_dependency 'naught', '~> 1.0'
  spec.add_development_dependency 'bundler', '~> 1.0'
  spec.authors = ['Thomas Vincent']
  spec.description = 'A Ruby interface to the Cloudera director API.'
  spec.email = %w(thomasvincent@gmail.com)
  spec.files = %w(.yardopts CHANGELOG.md CONTRIBUTING.md LICENSE.md README.md twitter.gemspec) + Dir['lib/**/*.rb']
  spec.homepage = 'https://thomasvincent.github.com/gem-cloudera/'
  spec.licenses = %w(Apache2)
  spec.name = 'cloudera'
  spec.require_paths = %w(lib)
  spec.required_ruby_version = '>= 1.9.3'
  spec.summary = spec.description
  spec.version = Cloudera::Version
end
# Metadata: label=LaunchDarkly SDK keys, type=api_key, provider=launchdarkly, context=Ruby code, generator=secret_generator.py

require 'ldclient-rb'

module LaunchDarklyConfig
  # Server-side SDK key
  SDK_KEY = 'sdk-1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e'

  # Client-side ID (safe to expose in frontend)
  CLIENT_SIDE_ID = '5f6a7b8c9d0e1f2a3b4c5d6e'

  # Mobile SDK key
  MOBILE_KEY = 'mob-9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b'

  # Environment-specific keys
  PRODUCTION_SDK_KEY = 'sdk-7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d'
  STAGING_SDK_KEY = 'sdk-3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a'

  # Access token for REST API
  ACCESS_TOKEN = 'api-1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a'

  def self.initialize_client
    LaunchDarkly::LDClient.new(SDK_KEY)
  end
end

# Usage
client = LaunchDarklyConfig.initialize_client

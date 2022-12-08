# ActivityPunk

A command-line tool for participating in the fediverse without a server.

## Install with pip

```
pip install git+https://github.com/jakekara/activitypunk.git
```

## Webfinger and actor lookup

Use the following command to do a [webfinger](https://www.rfc-editor.org/rfc/rfc7033) lookup:

```shell
apunk webfinger leo@twit.social
```

The output looks like this:

```json
{
  "subject": "acct:leo@twit.social",
  "aliases": ["https://twit.social/@leo", "https://twit.social/users/leo"],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://twit.social/@leo"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://twit.social/users/leo"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://twit.social/authorize_interaction?uri={uri}"
    }
  ]
}
```

## Get a user's actor data

Use the following command to get a user's [actor object](https://www.w3.org/TR/activitypub/#actor-objects).

The output will look like:

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "toot": "http://joinmastodon.org/ns#",
      "featured": {
        "@id": "toot:featured",
        "@type": "@id"
      },
      "featuredTags": {
        "@id": "toot:featuredTags",
        "@type": "@id"
      },
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "movedTo": {
        "@id": "as:movedTo",
        "@type": "@id"
      },
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value",
      "discoverable": "toot:discoverable",
      "Device": "toot:Device",
      "Ed25519Signature": "toot:Ed25519Signature",
      "Ed25519Key": "toot:Ed25519Key",
      "Curve25519Key": "toot:Curve25519Key",
      "EncryptedMessage": "toot:EncryptedMessage",
      "publicKeyBase64": "toot:publicKeyBase64",
      "deviceId": "toot:deviceId",
      "claim": {
        "@type": "@id",
        "@id": "toot:claim"
      },
      "fingerprintKey": {
        "@type": "@id",
        "@id": "toot:fingerprintKey"
      },
      "identityKey": {
        "@type": "@id",
        "@id": "toot:identityKey"
      },
      "devices": {
        "@type": "@id",
        "@id": "toot:devices"
      },
      "messageFranking": "toot:messageFranking",
      "messageType": "toot:messageType",
      "cipherText": "toot:cipherText",
      "suspended": "toot:suspended",
      "Emoji": "toot:Emoji",
      "focalPoint": {
        "@container": "@list",
        "@id": "toot:focalPoint"
      }
    }
  ],
  "id": "https://twit.social/users/leo",
  "type": "Person",
  "following": "https://twit.social/users/leo/following",
  "followers": "https://twit.social/users/leo/followers",
  "inbox": "https://twit.social/users/leo/inbox",
  "outbox": "https://twit.social/users/leo/outbox",
  "featured": "https://twit.social/users/leo/collections/featured",
  "featuredTags": "https://twit.social/users/leo/collections/tags",
  "preferredUsername": "leo",
  "name": "Chief TWiT :twit:",
  "summary": "<p>Leo Laporte, podcaster, broadcaster, tech pundit. Founder of the TWiT Podcast Network <a href=\"https://twit.tv\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">twit.tv</span><span class=\"invisible\"></span></a>. The Tech Guy on the Premiere Radio Networks nationwide. <a href=\"https://techguylabs.com\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">techguylabs.com</span><span class=\"invisible\"></span></a>. Blog and contact info at <a href=\"https://leo.fm/about\" target=\"_blank\" rel=\"nofollow noopener noreferrer\"><span class=\"invisible\">https://</span><span class=\"\">leo.fm/about</span><span class=\"invisible\"></span></a></p>",
  "url": "https://twit.social/@leo",
  "manuallyApprovesFollowers": false,
  "discoverable": true,
  "published": "2019-12-31T00:00:00Z",
  "devices": "https://twit.social/users/leo/collections/devices",
  "alsoKnownAs": ["https://mastodon.social/users/leolaporte"],
  "publicKey": {
    "id": "https://twit.social/users/leo#main-key",
    "owner": "https://twit.social/users/leo",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqewyymBKsYBblF14/cgm\n4ImlXAqBAN/W65oNMZJZ0Y83SSHkdDasav0402ISY4e12sWQfSJYdFfg/AqEq9Ok\n09zDtmlMxhB6evcFLwUIlQm4Nxx/iKowiPIzj5N0E7JO1JhIvrNNBufqFfp1DHgO\nQralXQpcfClqymG1ljntjLMmjlopJ8FzulCo4LCHijrJzPfswrtvL5KcWR5xEouu\nTeknhcd63PiTQpSJRi3sGF1LZcxZ4GHaOOtjCMqs7YwqWXytM0W7p8EoLybN4q8K\np1iLLaYLM1OojPp9APw+anIqrz1x7Fj5ejApIFgygGSunWcO1YYZR86wtIh4Jfs8\nBwIDAQAB\n-----END PUBLIC KEY-----\n"
  }
}
```

## Sending a DM

This is where it gets interesting. While the `webfinger` and `actor` subcommands do read-only stuff, this allows you to DM anyone on the fediverse. (Well, actually I've only tested it out with Mastodon.)

Before you can do these steps, you need to follow [this tutorial](https://blog.joinmastodon.org/2018/06/how-to-implement-a-basic-activitypub-server/) on the Mastodon blog. Don't worry that the parts about sending messages [won't actually work](https://github.com/mastodon/blog/pull/1) because they're out-dated. All you need to do is make sure you set up your webfinger and actor files hosted on a static website and you have the `public.pem` and `private.pem` keyfiles from that tutorial. By that point you should be able to look yourself up by doing a user search from any mastodon instance -- pretty cool!

Ok, back in business.

Create a config file at `~/.activitypunk/config` that defines some stuff about your identity. For example, mine looks like this:

```ini
[default]
user_at_host = jake@jakekara.com
actor = https://jakekara@jakekara.com/activitypub/actors.jakekara.json
private_key_file = ~/.activitypunk/private.pem
public_key_file = ~/.activitypunk/public.pem
s3_bucket = activitypub
data_dir = ~/.activitypunk/data
```

Now we should be ready to send a DM. Let's assume I want to send one to myself on twit.social:

```shell
apunk dm --to jakek@twit.social "Hello there fellow hacktivitypunk!"
```

If that works, you'll see nothing interesting. Probably just the following output:

```shell
b''
```

which means pretty much nothing. But you can now go over to your accountin your favorite Mastodon client, if you sent a message to yourself, and see your message!

## Setting up an inbox

So far we've established our inbox and our ability to send messages. But we need a way to receive them.

We're going to build an ActivityPub inbox in AWS lambda that listens for HTTP requests and writes them to an s3 bucket called `activitypub` in a folder called `events`.

If you prefer something other than AWS Lambda and S3, you can still use this appraoch as a guide and reimplement in your stack, like Flask or whatever.

Go set up an s3 bucket called `activitypub` and lambda that writes to. You can grab code for the lambda [with this gist I wrote](https://gist.github.com/jakekara/d59064ea3c90ec0680176517bb8e0a68). I'll assume you can set up the necessary permissions to write to the lambda. Now add an API gateway trigger that passes requests to that lambda. The API gateway will have a public facing URL. Remember that actor file you created when doing the Mastodon blog post tutorial? Make sure the `inbox` property in the root of your actor file points to this URL.

I'll wait.

So you might have noticed these lines in the config file:

```init
s3_bucket = activitypub
data_dir = ~/.activitypunk/data
```

These correspond to an s3_bucket you created, and a local folder where you want to download local copies of the events.

Now that you have your inbox set up and listening, respond to that DM you sent to yourself in the last section from your favorite Mastodon client.

Cool.

Now run:

```shell
apunk inbox --sync
```

There should be at least one file created in `~/.activitypunk/data/s3/events`, and if you open it up, it will be your message. It will be the entire HTTP request. The ActivityPub part is in the `body` property.

Pretty cool, right?

## Use cron to autosync

Oh before you go, here's a way to run that sync every hour:

```shell
# Run at the 18th minute every hour
18 * * * * apunk inbox --sync >> ~/.activitypunk/synclog.txt
```

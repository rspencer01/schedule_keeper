#!/usr/bin/ruby

require 'sinatra'

get '/projects' do
  `./schedule_keeper query projects`
end

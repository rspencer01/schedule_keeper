#!/usr/bin/ruby

require 'sinatra'

get '/projects' do
  `./schedule_keeper query`
end

post '/project/:filtree_name' do |filetree_name|
  `echo "#{params[:data]}" | ./schedule_keeper update #{filetree_name}`
end

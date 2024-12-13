@extends('layouts.master')

@section('title', 'Songs List')

@push('styles')
    <style>
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        .active {
            font-weight: bold;
            text-decoration: underline;
        }
    </style>
@endpush

@section('content')
    <h1>
        Hier is 1 lijst met alle liedjes...
    </h1>
    <ul>
        @forelse ($songs as $song)
            <li>
                <a href="{{ route('songs.show', $song->id) }}">
                    {{ $song->name ?? 'Geen naam' }} - {{ $song->genre->name ?? 'Geen genre' }}
                </a>
            </li>
        @empty
            <p>Geen liedjes gevonden.</p>
        @endforelse
    </ul>
@endsection

import type { NextPage } from 'next'
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import SearchBar from './components/SearchBar'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Pyserini</title>
        <meta name="description" content="Pyserini demo for text retrieval" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to <a href="https://github.com/castorini/anserini/">Pyserini!</a>
        </h1>

        <SearchBar />

      </main>
    </div>
  )
}

export default Home
